# src/download_threads.py
import os
import threading
import shutil
import yt_dlp
from .video_info import VideoInfo
from .translations import get_text

# ------------ Exception spéciale pour une annulation propre ------------
class DownloadCancelled(Exception):
    """Exception interne utilisée pour signaler une annulation propre."""
    pass


# ------------------------------------------------------------------
# ⚠️ On NE force PLUS de liste de "player_client" ici.
# yt-dlp choisit lui-même, par défaut, les clients à essayer
# (ex: android_vr, qui contourne actuellement la restriction PO
# Token/SABR sur le client "web"). Cette logique est maintenue à
# jour en continu par les devs de yt-dlp pour suivre les
# changements de YouTube — un client codé en dur ici deviendrait
# vite obsolète et exclurait justement celui qui fonctionne.
# On garde uniquement un format avec fallback "/best" pour ne
# jamais planter si la combinaison demandée n'existe pas.
# ------------------------------------------------------------------
YOUTUBE_EXTRACTOR_ARGS = {}


# =========================== INFO THREAD ===============================
class InfoThread(threading.Thread):
    """
    Thread chargé UNIQUEMENT de récupérer les infos d'une vidéo.
    L'URL est supposée valide (déjà vérifiée par resolve_url).
    """

    def __init__(self, url, app, callback=None, error_callback=None):
        super().__init__()
        self.url = url
        self.app = app
        self.callback = callback
        self.error_callback = error_callback
        self.daemon = True

    def run(self):
        try:
            info = VideoInfo(self.url)
            info.fetch_info()

            if self.callback:
                self.callback(info)

        except Exception:
            # Erreur technique uniquement (yt-dlp, réseau, etc.)
            if self.error_callback:
                self.error_callback(
                    get_text("fetching_impossible", self.app.current_language)
                )

# ======================== DOWNLOAD THREAD =============================
class DownloadThread(threading.Thread):
    _used_filenames = set()
    _lock = threading.Lock()

    def __init__(self, url, app, download_type, resolution, bitrate, audio_format, output_path,
                 progress_callback=None, status_callback=None, finished_callback=None):
        """
        Thread qui télécharge soit :
            - une vidéo + audio (download_type = 'video')
            - un fichier audio seul (download_type = 'audio')

        progress_callback  : fonction appelée à chaque mise à jour du pourcentage
        status_callback    : fonction appelée pour afficher un texte de statut (vitesse, ETA…)
        finished_callback  : fonction appelée lorsqu'un téléchargement se termine
        """

        super().__init__()
        self.url = url
        self.app = app
        self.download_type = download_type
        self.resolution = resolution
        self.bitrate = bitrate
        self.audio_format = audio_format
        self.output_path = output_path

        self.progress_callback = progress_callback
        self.status_callback = status_callback
        self.finished_callback = finished_callback

        # Permet d'annuler un téléchargement proprement
        self.is_cancelled = False
        self.daemon = True

    # ----- Hook de progression -----
    def progress_hook(self, d):
        """
         d est un dictionnaire envoyé directement par yt-dlp.
         Il contient :
             - d["status"]       -> "downloading" ou "finished"
             - d["_percent_str"] -> "32.1%"
             - d["_speed_str"]   -> "1.2MiB/s"
             - d["_eta_str"]     -> "00:12"
         """

        # Gestion de l'annulation
        if self.is_cancelled:
            # On arrête proprement le téléchargement
            raise DownloadCancelled()

        status = d.get('status', '')
        if status == 'downloading':
            # Pourcentage brut envoyé à la barre de progression
            pct_str = d.get('_percent_str', '0%').replace('%', '').strip()
            try:
                pct = float(pct_str)
            except Exception:
                pct = 0.0

            if self.progress_callback:
                self.progress_callback(int(pct))

            if self.status_callback:
                self.status_callback(
                    f"{get_text('downloading', self.app.current_language)} "
                    f"{d.get('_speed_str', '')} - "
                    f"{get_text('remaining_time', self.app.current_language)} {d.get('_eta_str', '')}"  # temps restant
                )

        elif status == 'finished':
            # Quand yt-dlp a tout téléchargé
            if self.progress_callback:
                self.progress_callback(100)
            if self.status_callback:
                self.status_callback(get_text("processing_file", self.app.current_language))

    # ----- Génération de nom unique après téléchargement -----
    def get_unique_basename(self, base_name, ext):
        with self._lock:
            candidate = base_name
            counter = 1

            full_path = os.path.join(self.output_path, f"{candidate}.{ext}")

            while (
                    os.path.exists(full_path)
                    or f"{candidate}.{ext}" in self._used_filenames
            ):
                candidate = f"{base_name} ({counter})"
                full_path = os.path.join(self.output_path, f"{candidate}.{ext}")
                counter += 1

            # réserver le nom pour les autres threads
            self._used_filenames.add(f"{candidate}.{ext}")

            return candidate

    # ----- Exécution -----
    def run(self):
        try:
            # ----------------------------------------------------------
            # Récupérer le titre avant de construire ydl_opts
            # ⚠️ IMPORTANT : on DOIT donner un format explicite +
            # tolérant ici aussi, sinon yt-dlp résout le sélecteur par
            # défaut ("best") en interne et peut planter avec
            # "Requested format is not available" (SABR streaming)
            # avant même d'avoir tenté le vrai téléchargement plus bas.
            # ----------------------------------------------------------
            title_fetch_opts = {
                'quiet': True,
                'no_warnings': True,
                'format': 'bestvideo+bestaudio/best/all',
                'ignore_no_formats_error': True,
                'extractor_args': YOUTUBE_EXTRACTOR_ARGS,
            }
            with yt_dlp.YoutubeDL(title_fetch_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
                title = info.get('title', 'video')
                ext = 'mp4' if self.download_type == 'video' else ('mp3' if self.audio_format == 'mp3' else 'm4a')

                unique_title = self.get_unique_basename(title, ext)

            # Déterminer l'extension et générer un nom unique
            ext = 'mp4' if self.download_type == 'video' else ('mp3' if self.audio_format == 'mp3' else 'm4a')

            # ---------- Construction des options yt-dlp ----------
            # ⚠️ Comme pour BatchDownloadThread : on ne force plus les
            # extensions [ext=mp4]/[ext=m4a] en filtre dur. On laisse
            # yt-dlp choisir le meilleur flux disponible (avec
            # préférence mp4/m4a via format_sort) et on s'appuie sur
            # merge_output_format/FFmpegExtractAudio pour le résultat
            # final, avec un vrai fallback "/best" en bout de chaîne.

            # ----- VIDEO + AUDIO -----
            if self.download_type == "video":
                height = self.resolution[:-1] if self.resolution and self.resolution.endswith("p") else None

                format_str = "bestvideo"
                if height:
                    format_str = f"bestvideo[height<={height}]"

                if self.bitrate:
                    br = int(self.bitrate.replace(" kbps", ""))
                    format_str += f"+bestaudio[abr>={br-10}][abr<={br+10}]/bestaudio"
                else:
                    format_str += "+bestaudio"

                fallback = f"best[height<={height}]" if height else "best"
                format_str += f"/{fallback}/best"

                ydl_opts = {
                    'format': format_str,
                    'format_sort': ['res', 'ext:mp4:m4a'],
                    'outtmpl': os.path.join(self.output_path, f"{unique_title}.%(ext)s"),  # Ne pas mettre de (1), (2) ici
                    'progress_hooks': [self.progress_hook],
                    'quiet': True,
                    'no_warnings': True,
                    'merge_output_format': 'mp4',
                    'nooverwrites': False,
                    'extractor_args': YOUTUBE_EXTRACTOR_ARGS,
                }

            # ----- AUDIO ONLY -----
            else:

                # ----- M4A (pas de conversion) -----
                if self.audio_format == 'm4a':
                    audio_fmt = 'bestaudio'
                    if self.bitrate:
                        br = int(self.bitrate.replace(" kbps", ""))
                        audio_fmt = f'bestaudio[abr>={br-10}][abr<={br+10}]/bestaudio'
                    ydl_opts = {
                        'format': audio_fmt + '/best',
                        'format_sort': ['ext:m4a:mp3'],
                        'outtmpl': os.path.join(self.output_path, f"{unique_title}.%(ext)s"),
                        'progress_hooks': [self.progress_hook],
                        'quiet': True,
                        'no_warnings': True,
                        'nooverwrites': False,
                        'extractor_args': YOUTUBE_EXTRACTOR_ARGS,
                    }

                # ----- MP3 (conversion volontaire) -----
                else:
                    preferred_quality = self.bitrate.replace(" kbps", "") if self.bitrate else '192'
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'format_sort': ['ext:m4a:mp3'],
                        'outtmpl': os.path.join(self.output_path, f"{unique_title}.%(ext)s"),
                        'progress_hooks': [self.progress_hook],
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': preferred_quality,
                        }],
                        'quiet': True,
                        'no_warnings': True,
                        'nooverwrites': False,
                        'extractor_args': YOUTUBE_EXTRACTOR_ARGS,
                    }

            # ---------- Téléchargement ----------
            # Lancement réel du téléchargement
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])

            if self.status_callback:
                self.status_callback(get_text("download_complete", self.app.current_language))
            if self.finished_callback:
                self.finished_callback(True)

        # -------- Annulation propre --------
        except DownloadCancelled:
            if self.status_callback:
                self.status_callback(get_text("download_canceled", self.app.current_language))
            if self.finished_callback:
                self.finished_callback(False)

        # -------- Erreur réelle --------
        except Exception as e:
            if self.status_callback:
                self.status_callback(f"{get_text('error_prefix', self.app.current_language)} {e}")
            if self.finished_callback:
                self.finished_callback(False)

    def cancel(self):
        self.is_cancelled = True


# ========================= BATCH DOWNLOAD THREAD ========================
class BatchDownloadThread(threading.Thread):
    def __init__(self, urls, app, download_type, resolution, bitrate, output_path,
                 progress_callback=None, status_callback=None, finished_callback=None):
        super().__init__()
        self.urls = urls
        self.app = app
        self.download_type = download_type
        self.resolution = resolution
        self.bitrate = bitrate
        self.output_path = output_path
        self.progress_callback = progress_callback
        self.status_callback = status_callback
        self.finished_callback = finished_callback

        self.is_cancelled = False
        self.daemon = True

        self._total_urls = max(1, len([u for u in urls if u.strip()]))
        self.total_count = self._total_urls


    # ------------------------------------------------------------------
    # Hook de progression (factory)
    # ------------------------------------------------------------------
    def _progress_hook_factory(self, base_percent, video_index, video_title_ref):
        def hook(d):
            if self.is_cancelled:
                raise DownloadCancelled()

            status = d.get('status', '')
            if status == 'downloading':
                pct_str = d.get('_percent_str', '0%').replace('%', '').strip()
                try:
                    pct = float(pct_str)
                except Exception:
                    pct = 0.0

                total_pct = base_percent + (pct / self._total_urls)

                if self.progress_callback:
                    self.progress_callback(int(total_pct))

                if self.status_callback:
                    # Format 3 lignes comme Single
                    self.status_callback(
                        f"Vidéo {video_index} / {self._total_urls}\n"
                        f"{video_title_ref[0]}\n"
                        f"{d.get('_speed_str', '')} - {d.get('_eta_str', '')}"
                    )

            elif status == 'finished':
                if self.progress_callback:
                    self.progress_callback(
                        int(base_percent + (100 / self._total_urls))
                    )

        return hook

    # ------------------------------------------------------------------
    # Exécution principale
    # ------------------------------------------------------------------
    def run(self):
        successful = 0

        try:
            # ==========================================================
            # 🆕 1. RÉCUPÉRATION DES TITRES AVANT DOWNLOAD
            # ==========================================================
            titles = []

            title_fetch_opts = {
                'quiet': True,
                'format': 'bestvideo+bestaudio/best/all',
                'ignore_no_formats_error': True,
                'extractor_args': YOUTUBE_EXTRACTOR_ARGS,
            }
            with yt_dlp.YoutubeDL(title_fetch_opts) as ydl:
                for url in self.urls:
                    url = url.strip()
                    if not url:
                        titles.append("video")
                        continue

                    try:
                        info = ydl.extract_info(url, download=False)
                        titles.append(info.get("title", "video"))
                    except Exception:
                        titles.append("video")

            # ==========================================================
            # 🆕 2. DÉTECTION DES DOUBLONS
            # ==========================================================
            from collections import Counter

            counts = Counter(titles)

            # ==========================================================
            # 🆕 3. GÉNÉRATION DES NOMS UNIQUES
            # ==========================================================
            used = {}
            final_titles = []

            for title in titles:
                if counts[title] == 1:
                    # 👉 PAS DE DOUBLON → nom normal
                    final_titles.append(title)
                else:
                    # 👉 DOUBLON → toujours numéroter
                    index = used.get(title, 0) + 1
                    used[title] = index

                    final_titles.append(f"{title} ({index})")

            # ==========================================================
            # 🔁 BOUCLE PRINCIPALE
            # ==========================================================
            for i, raw_url in enumerate(self.urls):
                if self.is_cancelled:
                    raise DownloadCancelled()

                url = raw_url.strip()
                if not url:
                    continue

                # Variables pour ce téléchargement
                video_index = i + 1
                video_title_ref = ["Chargement..."]

                # NOM FORCÉ
                forced_title = final_titles[i]

                # Statut initial
                if self.status_callback:
                    self.status_callback(
                        f"{get_text('checking_url', self.app.current_language)} "
                        f"({video_index}/{self._total_urls})"
                    )

                base_percent = (i * 100) / self._total_urls

                # Hook spécifique à cette vidéo
                progress_hook = self._progress_hook_factory(
                    base_percent,
                    video_index,
                    video_title_ref
                )

                # --------------------------------------------------
                # OPTIONS yt-dlp
                # --------------------------------------------------
                # ⚠️ IMPORTANT : depuis le passage de YouTube au "SABR
                # streaming", les filtres durs [ext=mp4]/[ext=m4a]
                # provoquent souvent "Requested format is not available"
                # car certaines vidéos n'exposent plus ces flux pour le
                # client web. On utilise désormais "format_sort" pour
                # *préférer* mp4/m4a sans les exiger, avec un vrai
                # fallback "/best". Le merge_output_format='mp4' se
                # charge ensuite du remux/transcodage final via ffmpeg.

                if self.download_type == "video":

                    # CAS 1 — Best format (comme single tab)
                    if self.resolution == "Best":
                        ydl_opts = {
                            "format": "bestvideo+bestaudio/best",
                            "format_sort": ["res", "ext:mp4:m4a"],
                            "outtmpl": os.path.join(
                                self.output_path,
                                f"{forced_title}.%(ext)s"
                            ),
                            "progress_hooks": [progress_hook],
                            "quiet": True,
                            "no_warnings": True,
                            "merge_output_format": "mp4",
                            "nooverwrites": True,
                            "extractor_args": YOUTUBE_EXTRACTOR_ARGS,
                        }

                    # CAS 2 — Résolution contrôlée
                    else:
                        height = (
                            self.resolution[:-1]
                            if self.resolution.endswith("p")
                            else None
                        )

                        format_str = "bestvideo"
                        if height:
                            format_str = f"bestvideo[height<={height}]"

                        if self.bitrate and self.bitrate != "Best":
                            br = self.bitrate.replace(" kbps", "")
                            format_str += (
                                f"+bestaudio[abr>={int(br) - 10}]"
                                f"[abr<={int(br) + 10}]"
                            )
                        else:
                            format_str += "+bestaudio"

                        # Fallback : si la combinaison vidéo+audio filtrée
                        # n'existe pas, on retombe sur un "best" respectant
                        # au moins la hauteur, puis sur "best" tout court.
                        fallback = f"best[height<={height}]" if height else "best"
                        format_str += f"/{fallback}/best"

                        ydl_opts = {
                            "format": format_str,
                            "format_sort": ["res", "ext:mp4:m4a"],
                            "outtmpl": os.path.join(
                                self.output_path,
                                f"{forced_title}.%(ext)s"
                            ),
                            "progress_hooks": [progress_hook],
                            "quiet": True,
                            "no_warnings": True,
                            "merge_output_format": "mp4",
                            "nooverwrites": True,
                            "extractor_args": YOUTUBE_EXTRACTOR_ARGS,
                        }

                else:
                    preferred_quality = (
                        self.bitrate.replace(" kbps", "")
                        if (self.bitrate and self.bitrate != "Best")
                        else "192"
                    )

                    ydl_opts = {
                        "format": "bestaudio/best",
                        "format_sort": ["ext:m4a:mp3"],
                        "outtmpl": os.path.join(
                            self.output_path,
                            f"{forced_title}.%(ext)s"
                        ),
                        "progress_hooks": [progress_hook],
                        "postprocessors": [{
                            "key": "FFmpegExtractAudio",
                            "preferredcodec": "mp3",
                            "preferredquality": preferred_quality,
                        }],
                        "quiet": True,
                        "no_warnings": True,
                        "nooverwrites": True,
                        "extractor_args": YOUTUBE_EXTRACTOR_ARGS,
                    }

                # --------------------------------------------------
                # TÉLÉCHARGEMENT
                # --------------------------------------------------

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Récupérer le titre de la vidéo avant téléchargement
                    try:
                        info = ydl.extract_info(url, download=False)
                        video_title_ref[0] = info.get("title", "Titre inconnu")
                    except Exception:
                        video_title_ref[0] = "Titre inconnu"

                    # Mettre à jour le statut avec le format 3 lignes
                    if self.status_callback:
                        self.status_callback(
                            f"Vidéo {video_index} / {self._total_urls}\n"
                            f"{video_title_ref[0]}\n"
                            f"{get_text('downloading', self.app.current_language)}..."
                        )

                    # Maintenant télécharger pour de vrai
                    ydl.download([url])

                successful += 1

            # --------------------------------------------------
            # FIN NORMALE
            # --------------------------------------------------
            if self.status_callback:
                self.status_callback(
                    get_text("batch_download_complete", self.app.current_language)
                )

            if self.finished_callback:
                self.finished_callback(successful, self.total_count)

            # ------------------------------------------------------
            # ANNULATION
            # ------------------------------------------------------
        except DownloadCancelled:
            if self.status_callback:
                self.status_callback(
                    get_text("canceling_batch_download", self.app.current_language)
                )
            if self.finished_callback:
                self.finished_callback(successful, self.total_count)

            # ------------------------------------------------------
            # ERREUR RÉELLE
            # ------------------------------------------------------
        except Exception as e:
            if self.status_callback:
                self.status_callback(
                    f"{get_text('error_prefix', self.app.current_language)} {e}"
                )
            if self.finished_callback:
                self.finished_callback(successful, self.total_count)

    def cancel(self):
        self.is_cancelled = True