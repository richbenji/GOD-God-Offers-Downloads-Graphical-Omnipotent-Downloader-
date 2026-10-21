"""
Utilitaires communs pour gérer l'authentification yt-dlp face aux
vidéos privées / avec restriction d'âge, de façon cohérente entre
TOUS les points d'appel de l'application (résolution d'URL,
récupération d'infos, téléchargement simple, téléchargement batch).

Avant ce module, chaque fichier gérait les cookies un peu différemment,
ce qui faisait qu'une vidéo pouvait passer une étape (grâce aux
cookies Firefox automatiques) puis re-planter à l'étape suivante
(qui n'avait, elle, accès qu'à un cookies.txt manuel).

Ce module fournit aussi le runtime JavaScript (deno) embarqué avec
l'application, nécessaire à yt-dlp pour résoudre les challenges YouTube.
"""
import logging
import os
import re
import stat
import sys
from pathlib import Path

import yt_dlp

logger = logging.getLogger(__name__)

# Motifs qui indiquent qu'une erreur yt-dlp est probablement liée à
# une authentification manquante (vidéo privée, non répertoriée,
# restriction d'âge, playlist privée, etc.)
# "age" et "403" sont cherchés comme MOTS ENTIERS : sinon "age" matche
# "images", "language", "message", "page"... et "403" matche "14031".
AUTH_ERROR_PATTERN = re.compile(
    r"private|sign in|login|cookies|forbidden|\b403\b|\bage\b",
    re.IGNORECASE,
)

# Motifs qui indiquent que le CHARGEMENT des cookies a échoué (profil
# Firefox introuvable, base illisible, trousseau verrouillé...), et non
# que la vidéo pose problème. Ces erreurs ne doivent pas masquer la
# vraie cause de l'échec.
COOKIE_LOAD_ERROR_PATTERN = re.compile(
    r"cookies database|could not find .*cookies|keyring|"
    r"failed to (?:load|read) .*cookies",
    re.IGNORECASE,
)


class NoFormatsError(Exception):
    """
    Levée quand yt-dlp n'a renvoyé AUCUN vrai format (ni vidéo ni audio),
    typiquement : seules les images (storyboards) sont disponibles. Avec
    'ignore_no_formats_error', yt-dlp ne lève plus d'exception dans ce
    cas ; on la reconstruit donc ici pour pouvoir déclencher le fallback
    (cookies Firefox) puis informer l'UI.
    """


# ---------------------------------------------------------------------------
# Runtime JavaScript (deno) embarqué
# ---------------------------------------------------------------------------

def _runtime_dir() -> Path:
    """
    Dossier du runtime pour l'OS courant :
    resources/runtime/{linux,windows,macos}

    - depuis les sources : ce fichier est dans GOD/GOD/src/, les
      ressources sont dans GOD/GOD/resources/ (donc un niveau au-dessus)
    - depuis un exécutable PyInstaller : relatif à sys._MEIPASS
      (les ressources doivent être ajoutées avec la même arborescence
      relative, voir --add-data)
    """
    if sys.platform.startswith("win"):
        os_dir = "windows"
    elif sys.platform == "darwin":
        os_dir = "macos"
    else:
        os_dir = "linux"

    if hasattr(sys, "_MEIPASS"):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parent.parent
    return base / "resources" / "runtime" / os_dir


def get_deno_path():
    """
    Retourne le chemin du binaire deno embarqué, ou None s'il est absent.
    Dans ce cas, yt-dlp cherchera lui-même deno dans le PATH système.
    """
    is_windows = sys.platform.startswith("win")
    path = _runtime_dir() / ("deno.exe" if is_windows else "deno")
    if not path.is_file():
        return None

    # Le bit exécutable peut être perdu (copie, archive, PyInstaller...)
    if not is_windows and not os.access(path, os.X_OK):
        try:
            path.chmod(
                path.stat().st_mode
                | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
            )
        except OSError:
            return None
    return str(path)


_deno_missing_logged = False


def with_js_runtime(opts):
    """
    Retourne une copie des options yt-dlp avec le deno embarqué déclaré
    comme runtime JavaScript. À utiliser aussi partout où l'application
    crée un yt_dlp.YoutubeDL en dehors de ce module.
    Ne touche pas aux options si 'js_runtimes' est déjà défini.

    Si le deno embarqué est introuvable, un avertissement est affiché
    une seule fois (avec le chemin attendu) et yt-dlp cherche deno dans
    le PATH système.
    """
    global _deno_missing_logged

    new_opts = dict(opts)
    if "js_runtimes" in new_opts:
        return new_opts

    deno = get_deno_path()
    if not deno:
        if not _deno_missing_logged:
            _deno_missing_logged = True
            logger.warning(
                "deno embarqué introuvable ou non exécutable dans %s : "
                "yt-dlp cherchera deno dans le PATH système.",
                _runtime_dir(),
            )
        return new_opts

    # Filet de sécurité : yt-dlp active deno par défaut s'il le trouve
    # dans le PATH. On y ajoute donc aussi le dossier du deno embarqué,
    # ce qui fonctionne même si le format de 'js_runtimes' change.
    deno_dir = str(Path(deno).parent)
    current_path = os.environ.get("PATH", "")
    if deno_dir not in current_path.split(os.pathsep):
        os.environ["PATH"] = deno_dir + os.pathsep + current_path

    new_opts["js_runtimes"] = {"deno": {"path": deno}}
    return new_opts


# ---------------------------------------------------------------------------
# Détection des erreurs et des résultats vides
# ---------------------------------------------------------------------------

def is_auth_error(exc) -> bool:
    """Retourne True si l'exception ressemble à un problème d'authentification."""
    return bool(AUTH_ERROR_PATTERN.search(str(exc)))


def is_cookie_load_error(exc) -> bool:
    """
    Retourne True si l'exception vient du chargement des cookies
    (ex : profil Firefox introuvable) plutôt que de la vidéo elle-même.
    """
    if "cookieload" in type(exc).__name__.lower():
        return True
    return bool(COOKIE_LOAD_ERROR_PATTERN.search(str(exc)))


def _is_media_format(fmt) -> bool:
    """True pour un vrai flux vidéo/audio, False pour un storyboard (images)."""
    if fmt.get("ext") == "mhtml":
        return False
    return not (fmt.get("vcodec") == "none" and fmt.get("acodec") == "none")


def has_media_formats(info) -> bool:
    """
    True si 'info' contient au moins un vrai format vidéo ou audio.
    Une playlist est toujours considérée comme valide (ses entrées sont
    vérifiées individuellement plus tard).
    """
    if not info:
        return False
    if info.get("_type") == "playlist":
        return True
    return any(_is_media_format(f) for f in (info.get("formats") or []))


def _pick_exception(video_exc, cookie_exc):
    """
    Choisit l'exception la plus utile à remonter : celle de la vidéo
    (dernière tentative en date) si elle existe, sinon l'erreur de
    chargement des cookies.
    """
    return video_exc if video_exc is not None else cookie_exc


# ---------------------------------------------------------------------------
# Authentification et fallbacks
# ---------------------------------------------------------------------------

def build_auth_attempts(base_opts, cookies_path=None):
    """
    Construit la liste des options yt-dlp à essayer, dans l'ordre :

    1) Cookies MANUELS si déjà fournis (cookies.txt donné par
       l'utilisateur via le popup) ET que le fichier existe encore
       sur le disque, sinon aucune authentification. Le fichier peut
       avoir été déplacé/supprimé depuis la dernière session (le
       chemin est persisté dans config.json sans revérification) —
       dans ce cas on ignore silencieusement ce chemin invalide au
       lieu de planter avec une erreur confuse.
    2) Cookies AUTOMATIQUES depuis Firefox, en fallback — utile pour
       le contenu privé/restreint de l'utilisateur s'il est connecté
       à YouTube dans Firefox. On ne le met JAMAIS en 1ère position
       pour ne pas dépendre de Firefox sur du contenu public.

    Le runtime JavaScript embarqué est ajouté à chaque tentative.
    """
    base_opts = with_js_runtime(base_opts)

    attempts = []
    if cookies_path and os.path.isfile(cookies_path):
        attempts.append({**base_opts, "cookiefile": cookies_path})
    else:
        attempts.append(dict(base_opts))

    attempts.append({**base_opts, "cookiesfrombrowser": ("firefox",)})
    return attempts


def extract_info_with_fallback(url, base_opts, cookies_path=None,
                               require_formats=False):
    """
    Essaie ydl.extract_info() avec plusieurs stratégies d'authentification
    successives. Renvoie le résultat dès qu'une stratégie fonctionne.

    require_formats=True : une tentative qui ne renvoie aucun vrai format
    vidéo/audio (par ex. seulement des images, parce que
    'ignore_no_formats_error' masque l'erreur de yt-dlp) est considérée
    comme un échec, et on passe à la stratégie suivante. À utiliser pour
    récupérer la liste des formats d'une vidéo.

    Si toutes échouent, lève par ordre de priorité :
      1) l'erreur LIÉE À LA VIDÉO de la dernière tentative concernée ;
      2) NoFormatsError si aucune tentative n'a renvoyé de format ;
      3) l'erreur de chargement des cookies, s'il n'y a rien d'autre.
    """
    video_exc = None
    cookie_exc = None
    no_formats = False

    for opts in build_auth_attempts(base_opts, cookies_path):
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
        except Exception as e:
            if is_cookie_load_error(e):
                cookie_exc = e
            else:
                video_exc = e
            continue

        if require_formats and not has_media_formats(info):
            no_formats = True
            continue

        return info

    if video_exc is not None:
        raise video_exc
    if no_formats:
        raise NoFormatsError(
            "Aucun format vidéo/audio disponible (seules des images ont "
            "été renvoyées)."
        )
    raise cookie_exc


def download_with_fallback(url, base_opts, cookies_path=None):
    """
    Essaie ydl.download() avec plusieurs stratégies d'authentification.
    Ne réessaie AVEC UNE AUTRE SOURCE DE COOKIES que si l'échec
    ressemble à un problème d'authentification — sinon (ex: annulation
    utilisateur, erreur réseau) on relance l'exception immédiatement,
    pas la peine de retélécharger inutilement.

    Comme pour extract_info_with_fallback, une erreur de chargement des
    cookies ne masque pas l'erreur de la vidéo.
    """
    video_exc = None
    cookie_exc = None

    for opts in build_auth_attempts(base_opts, cookies_path):
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            return
        except Exception as e:
            # À tester AVANT is_auth_error : le message d'une erreur de
            # cookies contient le mot "cookies" et ressemblerait sinon
            # à un problème d'authentification.
            if is_cookie_load_error(e):
                cookie_exc = e
                continue
            video_exc = e
            if not is_auth_error(e):
                raise

    raise _pick_exception(video_exc, cookie_exc)