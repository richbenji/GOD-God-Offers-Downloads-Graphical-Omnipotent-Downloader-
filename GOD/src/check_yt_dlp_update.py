import yt_dlp
import requests
from packaging import version

def check_yt_dlp_update():
    """Vérifie si yt-dlp est à jour, et propose une mise à jour si nécessaire."""
    try:
        # Version locale
        local_version = yt_dlp.version.__version__

        # Dernière version dispo sur PyPI
        latest_version = requests.get(
            "https://pypi.org/pypi/yt-dlp/json", timeout=5
        ).json()["info"]["version"]

        if version.parse(local_version) < version.parse(latest_version):
            # Pas à jour → notifier l’utilisateur
            from tkinter import messagebox
            answer = messagebox.askyesno(
                "Mise à jour disponible",
                f"Votre version de yt-dlp est {local_version}, "
                f"la dernière est {latest_version}.\n\n"
                f"Voulez-vous mettre à jour automatiquement ?"
            )
            if answer:
                import subprocess, sys
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
                    messagebox.showinfo("Mise à jour réussie", "yt-dlp a été mis à jour avec succès.\nRelancez l'application.")
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible de mettre à jour yt-dlp.\n\n{e}")
        else:
            print(f"✅ yt-dlp est à jour ({local_version})")

    except Exception as e:
        print(f"⚠️ Impossible de vérifier la mise à jour yt-dlp : {e}")