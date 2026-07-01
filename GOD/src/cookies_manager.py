from .config_manager import set_cookies_path, get_cookies_path


def init_cookies():
    """
    Chargé au démarrage de l'application.
    Retourne le chemin des cookies s'il existe et est valide.
    """
    path = get_cookies_path()
    return path if path else None


def update_cookies_path(path: str | None):
    """
    Met à jour la source de cookies (ou la supprime).
    """
    if path:
        set_cookies_path(path)
        return path

    set_cookies_path(None)
    return None
