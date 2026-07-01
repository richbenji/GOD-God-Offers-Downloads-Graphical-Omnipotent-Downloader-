import sys
import os

def resource_path(relative_path):
    """
    Retourne le chemin correct vers une ressource
    (fonctionne en dev ET avec PyInstaller)
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

   #Autre façon de faire :
   #try:
   #    base_path = sys._MEIPASS
   #except Exception:
   #    base_path = os.path.abspath(".")
   #return os.path.join(base_path, relative_path)
