from pathlib import Path
import customtkinter as ctk
import markdown
from PIL._tkinter_finder import tk
from tkinterweb import HtmlFrame
from .translations import get_text


BASE_DIR = Path(__file__).resolve().parent.parent
TUTORIAL_DIR = BASE_DIR / "assets" / "tutorials"


class TutorialTab:
    def __init__(self, parent, app):
        self.app = app
        self.parent = parent

        # Conteneur principal
        self.container = ctk.CTkFrame(parent)
        self.container.pack(fill="both", expand=True, padx=0, pady=0)

        # Charger le tutoriel
        self.load_tutorial()

    def load_tutorial(self):
        """Charge et affiche le tutoriel Markdown"""

        tutorial_file = TUTORIAL_DIR / f"tutorial_{self.app.current_language}.md"

        if not tutorial_file.exists():
            tutorial_file = TUTORIAL_DIR / "tutorial_en.md"

        if not tutorial_file.exists():
            self._show_placeholder()
            return

        # Lire le Markdown
        with open(tutorial_file, "r", encoding="utf-8") as f:
            md_content = f.read()

        # Convertir en HTML
        html_body = self.markdown_to_html(md_content)

        # Ajouter le CSS
        full_html = self.wrap_html(html_body)

        # Afficher avec HtmlFrame
        try:
            self.html_frame = HtmlFrame(self.container, messages_enabled=False)
            self.html_frame.load_html(full_html)
            self.html_frame.pack(fill="both", expand=True)
        except Exception as e:
            print("⚠️ HTML renderer indisponible :", e)

            # fallback UI simple
            #fallback = tk.Label(
            #    self.container,
            #    text="Le tutoriel HTML n'est pas disponible.\nVersion simplifiée affichée.",
            #    justify="center"
            #)
            #fallback.pack(fill="both", expand=True)

    def _show_placeholder(self):
        """Affiche un message si aucun tutoriel n'est disponible"""
        label = ctk.CTkLabel(
            self.container,
            text="📚 " + get_text("no_tutorial_available", self.app.current_language),
            font=ctk.CTkFont(size=16)
        )
        label.pack(pady=50)

    def markdown_to_html(self, md_text: str) -> str:
        """Convertit le Markdown en HTML"""
        return markdown.markdown(
            md_text,
            extensions=['fenced_code', 'tables', 'nl2br']
        )

    def wrap_html(self, body: str) -> str:
        """Enveloppe le HTML avec CSS adapté au thème"""

        text_color = "#ffffff" if self.app.appearance_mode == "dark" else "#000000"
        bg_color = "#2b2b2b" if self.app.appearance_mode == "dark" else "#ffffff"
        code_bg = "#1e1e1e" if self.app.appearance_mode == "dark" else "#f5f5f5"
        link_color = "#3B8ED0" if self.app.appearance_mode == "dark" else "#1f538d"
        border_color = "#444444" if self.app.appearance_mode == "dark" else "#d1d5da"

        css = f"""
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: {text_color};
            background-color: {bg_color};
            padding: 30px;
            max-width: 900px;
            margin: 0 auto;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: {text_color};
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
        }}

        h1 {{
            font-size: 2em;
            border-bottom: 2px solid {link_color};
            padding-bottom: 10px;
        }}

        h2 {{
            font-size: 1.5em;
            border-bottom: 1px solid {border_color};
            padding-bottom: 8px;
        }}

        h3 {{ font-size: 1.25em; }}

        p {{ margin-bottom: 16px; }}

        a {{
            color: {link_color};
            text-decoration: none;
        }}

        a:hover {{ text-decoration: underline; }}

        code {{
            background-color: {code_bg};
            color: {text_color};
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
        }}

        pre {{
            background-color: {code_bg};
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            border: 1px solid {border_color};
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
        }}

        ul, ol {{
            margin-bottom: 16px;
            padding-left: 32px;
        }}

        li {{ margin-bottom: 8px; }}

        blockquote {{
            border-left: 4px solid {link_color};
            padding-left: 16px;
            margin: 16px 0;
            color: #888888;
            font-style: italic;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
        }}

        th, td {{
            border: 1px solid {border_color};
            padding: 10px;
            text-align: left;
        }}

        th {{
            background-color: {code_bg};
            font-weight: 600;
        }}

        hr {{
            border: none;
            border-top: 2px solid {border_color};
            margin: 24px 0;
        }}
        """

        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>{css}</style>
</head>
<body>{body}</body>
</html>"""

    def refresh_theme(self):
        """Recharge le tutoriel avec le nouveau thème"""
        for widget in self.container.winfo_children():
            widget.destroy()
        self.load_tutorial()

    def refresh_texts(self):
        """Met à jour la langue du tutoriel"""
        for widget in self.container.winfo_children():
            widget.destroy()
        self.load_tutorial()