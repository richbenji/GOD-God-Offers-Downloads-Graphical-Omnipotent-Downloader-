import json
from pathlib import Path

APP_NAME = "ytdl_gui"
CONFIG_DIR = Path.home() / ".config" / APP_NAME
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config():
    if not CONFIG_FILE.exists():
        return {}

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_config(data: dict):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_cookies_path():
    cfg = load_config()
    path = cfg.get("cookies_path")
    return path if path else None


def set_cookies_path(path: str | None):
    cfg = load_config()
    if path:
        cfg["cookies_path"] = path
        cfg["cookies_source"] = "file"
    else:
        cfg.pop("cookies_path", None)
        cfg.pop("cookies_source", None)

    save_config(cfg)
