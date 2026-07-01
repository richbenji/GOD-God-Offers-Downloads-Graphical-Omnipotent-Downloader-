"""
Utilitaires communs pour gérer l'authentification yt-dlp face aux
vidéos privées / avec restriction d'âge, de façon cohérente entre
TOUS les points d'appel de l'application (résolution d'URL,
récupération d'infos, téléchargement simple, téléchargement batch).

Avant ce module, chaque fichier gérait les cookies un peu différemment,
ce qui faisait qu'une vidéo pouvait passer une étape (grâce aux
cookies Firefox automatiques) puis re-planter à l'étape suivante
(qui n'avait, elle, accès qu'à un cookies.txt manuel).
"""
import os
import yt_dlp

# Mots-clés qui indiquent qu'une erreur yt-dlp est probablement liée à
# une authentification manquante (vidéo privée, non répertoriée,
# restriction d'âge, playlist privée, etc.)
AUTH_ERROR_KEYWORDS = (
    "private",
    "sign in",
    "login",
    "cookies",
    "forbidden",
    "403",
    "age",
)


def is_auth_error(exc) -> bool:
    """Retourne True si l'exception ressemble à un problème d'authentification."""
    msg = str(exc).lower()
    return any(k in msg for k in AUTH_ERROR_KEYWORDS)


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
    """
    attempts = []
    if cookies_path and os.path.isfile(cookies_path):
        attempts.append({**base_opts, "cookiefile": cookies_path})
    else:
        attempts.append(dict(base_opts))

    attempts.append({**base_opts, "cookiesfrombrowser": ("firefox",)})
    return attempts


def extract_info_with_fallback(url, base_opts, cookies_path=None):
    """
    Essaie ydl.extract_info() avec plusieurs stratégies d'authentification
    successives. Renvoie le résultat dès qu'une stratégie fonctionne.
    Lève la DERNIÈRE exception rencontrée si toutes échouent.
    """
    last_exc = None
    for opts in build_auth_attempts(base_opts, cookies_path):
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            last_exc = e
            continue
    raise last_exc


def download_with_fallback(url, base_opts, cookies_path=None):
    """
    Essaie ydl.download() avec plusieurs stratégies d'authentification.
    Ne réessaie AVEC UNE AUTRE SOURCE DE COOKIES que si l'échec
    ressemble à un problème d'authentification — sinon (ex: annulation
    utilisateur, erreur réseau) on relance l'exception immédiatement,
    pas la peine de retélécharger inutilement.
    """
    attempts = build_auth_attempts(base_opts, cookies_path)
    last_exc = None

    for opts in attempts:
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            return
        except Exception as e:
            last_exc = e
            if not is_auth_error(e):
                raise
            continue

    raise last_exc