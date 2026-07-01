from urllib.parse import urlparse
import yt_dlp
from .errors import InvalidURLError, VideoInfoFetchError


def _is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def extract_playlist_entries(url, cookies_path=None):

    if not url or not isinstance(url, str) or not url.strip():
        raise InvalidURLError()

    if not _is_valid_url(url):
        raise InvalidURLError()

    base_opts = {
        "quiet": True,
        "skip_download": True,
        "no_warnings": True,
        "ignoreerrors": False,
    }

    strategies = [
        # 1) SANS cookies — cas normal, la grande majorité des vidéos
        #    et playlists publiques. On essaie toujours ça en premier
        #    pour ne JAMAIS dépendre de Firefox pour du contenu public.
        {
            **base_opts,
            "extract_flat": True,
        },
        # 2) Cookies AUTOMATIQUES depuis Firefox — utile pour TES
        #    propres playlists privées si tu es connecté à YouTube
        #    dans Firefox. On l'essaie seulement en 2e position (pas
        #    en 1er) : si Firefox n'est pas installé ou son profil
        #    inaccessible, ça échoue silencieusement ici et on
        #    continue vers la stratégie suivante, au lieu de faire
        #    planter TOUTE récupération (c'était le bug précédent).
        {
            **base_opts,
            "extract_flat": True,
            "cookiesfrombrowser": ("firefox",),
        },
        # 3) Cookies MANUELS (cookies.txt fourni par l'utilisateur via
        #    le popup), si on en a déjà un suite à une demande
        #    précédente dans cette session.
        {
            **base_opts,
            "extract_flat": False,
            "cookiefile": cookies_path,
        } if cookies_path else None,
    ]

    # Si au moins une tentative échoue avec une erreur qui ressemble à
    # un besoin d'authentification, on le retient pour, au pire, guider
    # l'utilisateur vers le popup de cookies manuel à la fin.
    needs_cookies = False

    for ydl_opts in filter(None, strategies):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            if not info:
                continue

            if info.get("_type") != "playlist":
                title = info.get("title")
                video_url = info.get("webpage_url")
                if not title or not video_url:
                    continue

                return [{
                    "url": video_url,
                    "title": title,
                    "index": 1
                }]

            raw_entries = info.get("entries")
            if not raw_entries:
                continue

            entries = []
            for idx, entry in enumerate(raw_entries, start=1):
                if not entry:
                    continue

                video_id = entry.get("id")
                title = entry.get("title") or f"Video {idx}"
                if not video_id:
                    continue

                entries.append({
                    "url": f"https://www.youtube.com/watch?v={video_id}",
                    "title": title,
                    "index": idx
                })

            if entries:
                return entries

        except Exception as e:
            msg = str(e).lower()
            # ⚠️ "403 Forbidden" est ajouté ici : YouTube renvoie ça
            # pour une playlist privée sans authentification, mais ça
            # ne contient ni "private" ni "sign in" — sans ce mot-clé,
            # l'erreur passait inaperçue et on tombait direct sur le
            # message générique "fetching_impossible".
            if any(k in msg for k in ("private", "sign in", "login", "cookies", "forbidden", "403")):
                needs_cookies = True
            continue

    if needs_cookies:
        raise VideoInfoFetchError("playlist_private")

    raise VideoInfoFetchError("fetching_impossible")