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
        # ⚠️ On NE force PAS de player_client ici non plus : yt-dlp
        # choisit lui-même les clients à essayer en interne. En mode
        # extract_flat, ça n'a de toute façon pas d'impact direct
        # puisqu'aucun format n'est résolu à ce stade.
    }

    strategies = [
        # 1) Tentative SANS cookies (cas normal, la grande majorité des cas).
        #    ⚠️ On ne force plus "cookiesfrombrowser": ("firefox",) ici :
        #    si Firefox n'est pas installé, ou que son profil cookies
        #    n'est pas accessible, yt-dlp levait une exception et CETTE
        #    étape échouait systématiquement, même pour une vidéo
        #    publique tout à fait normale.
        {
            **base_opts,
            "extract_flat": True,
        },
        # 2) Si on a déjà un fichier de cookies fourni par l'utilisateur
        #    (suite à une erreur "playlist_private" précédente), on
        #    retente avec.
        {
            **base_opts,
            "extract_flat": False,
            "cookiefile": cookies_path,
        } if cookies_path else None,
    ]

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
            if any(k in msg for k in ("private", "sign in", "login", "cookies")):
                raise VideoInfoFetchError("playlist_private")
            continue

    raise VideoInfoFetchError("fetching_impossible")