import os
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
from .translations import get_text
from .paths import resource_path


# --------------------------------------------------
# POLICES
# --------------------------------------------------

_loaded_fonts = set()  # évite de recharger la police plusieurs fois


def load_custom_font(font_relative_path, size=28, weight="bold", fallback=("Arial", 28, "bold")):
    """
    Charge une police custom compatible PyInstaller.
    """

    try:
        font_path = resource_path(font_relative_path)

        if os.path.exists(font_path):
            if font_path not in _loaded_fonts:
                ctk.FontManager.load_font(font_path)
                _loaded_fonts.add(font_path)

            if "TradeGothic" in font_path or "Trade Gothic" in font_path:
                family_name = "TradeGothic"  # 👈 Le vrai nom !
            else:
                family_name = os.path.splitext(os.path.basename(font_path))[0]

                # 👇 Pas de weight="bold" car la police est déjà en Bold
            return ctk.CTkFont(
                family=family_name,
                size=size
            )

    except Exception as e:
        print(f"Erreur lors du chargement de la police: {e}")

    # Fallback sécurisé
    return ctk.CTkFont(
        family=fallback[0],
        size=fallback[1],
        weight=fallback[2]
    )


# --------------------------------------------------
# IMAGES
# --------------------------------------------------

def load_logo_image(image_relative_path, size=(80, 80)):
    """
    Charge une image (logo, icône…) compatible PyInstaller.
    """
    try:
        image_path = resource_path(image_relative_path)

        if os.path.exists(image_path):
            pil_image = Image.open(image_path).resize(
                size, Image.Resampling.LANCZOS
            )
            return ctk.CTkImage(
                light_image=pil_image,
                dark_image=pil_image,
                size=size
            )

    except Exception as e:
        print(f"Erreur lors du chargement du logo: {e}")

    return None


# --------------------------------------------------
# BOÎTES DE DIALOGUE
# --------------------------------------------------

def ask_output_folder(language, last_folder=None):
    """
    Ouvre une boîte de dialogue pour choisir un dossier de sortie.
    """
    initialdir = last_folder if last_folder else os.path.expanduser("~")

    folder = filedialog.askdirectory(
        title=get_text("select_output_folder", language),
        initialdir=initialdir
    )
    return folder or None


def ask_cookies_file(language):
    """
    Demande à l'utilisateur de sélectionner un fichier cookies.txt
    """
    path = filedialog.askopenfilename(
        title=get_text("select_cookies_file", language),
        filetypes=[("Cookies file", "*.txt")]
    )
    return path or None


# --------------------------------------------------
# UTILITAIRES
# --------------------------------------------------

def format_bytes_iec(size_bytes, precision=2):
    """
    Convertit une taille en octets vers o / KiB / MiB / GiB / TiB (IEC).
    """
    if size_bytes is None:
        return "N/A"

    try:
        size_bytes = float(size_bytes)
    except (TypeError, ValueError):
        return "N/A"

    units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]
    factor = 1024.0

    for unit in units:
        if size_bytes < factor:
            return f"{size_bytes:.{precision}f} {unit}"
        size_bytes /= factor

    return f"{size_bytes:.{precision}f} PiB"
