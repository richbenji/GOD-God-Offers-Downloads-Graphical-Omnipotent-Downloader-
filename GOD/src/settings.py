from pathlib import Path

# Dossier de config de l'app
APP_DIR = Path.home() / ".ultimate_ytdlp_gui"
APP_DIR.mkdir(exist_ok=True)

# Cookies
COOKIES_FILE = APP_DIR / "cookies.txt"

# Activer / désactiver l'accès privé
ENABLE_PRIVATE_PLAYLISTS = True
