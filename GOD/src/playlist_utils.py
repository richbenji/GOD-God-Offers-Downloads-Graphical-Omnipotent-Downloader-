from urllib.parse import urlparse
from .errors import InvalidURLError, VideoInfoFetchError
from .yt_dlp_helpers import extract_info_with_fallback, is_auth_error


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
        "extract_flat": True,
        # ⚠️ Même en extract_flat=True, une URL de vidéo unique (pas une
        # playlist) est entièrement traitée par yt-dlp, y compris la
        # résolution de format. Sans sélecteur permissif ici, ça peut
        # planter avec "Requested format is not available" (SABR),
        # même pour une simple vérification d'URL.
        "format": "bestvideo+bestaudio/best/all",
        "ignore_no_formats_error": True,
    }

    try:
        # Essaie sans cookies, PUIS avec cookies Firefox automatiques
        # en fallback (utile pour les playlists privées / vidéos avec
        # restriction d'âge si tu es connecté à YouTube dans Firefox).
        info = extract_info_with_fallback(url, base_opts, cookies_path=cookies_path)
    except Exception as e:
        if is_auth_error(e):
            raise VideoInfoFetchError("playlist_private") from e
        raise VideoInfoFetchError("fetching_impossible") from e

    if not info:
        raise VideoInfoFetchError("fetching_impossible")

    if info.get("_type") != "playlist":
        title = info.get("title")
        video_url = info.get("webpage_url")
        if not title or not video_url:
            raise VideoInfoFetchError("fetching_impossible")

        return [{
            "url": video_url,
            "title": title,
            "index": 1
        }]

    raw_entries = info.get("entries")
    if not raw_entries:
        raise VideoInfoFetchError("fetching_impossible")

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

    if not entries:
        raise VideoInfoFetchError("fetching_impossible")

    return entries