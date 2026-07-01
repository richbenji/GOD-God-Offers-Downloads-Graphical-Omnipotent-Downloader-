from pathlib import Path
import re
import customtkinter as ctk

from .translations import get_text


BASE_DIR = Path(__file__).resolve().parent.parent
TUTORIAL_DIR = BASE_DIR / "assets" / "tutorials"


# =========================================================
# MARKDOWN VIEWER (INTÉGRÉ DANS LE MÊME FICHIER)
# =========================================================
class MarkdownViewer(ctk.CTkScrollableFrame):
    def __init__(self, parent, markdown_text: str):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        self.render(markdown_text)

    def render(self, text: str):
        lines = text.split("\n")

        in_code = False
        code_buffer = []

        for line in lines:

            # CODE BLOCK
            if line.strip().startswith("```"):
                if not in_code:
                    in_code = True
                    code_buffer = []
                else:
                    in_code = False
                    self._add_code("\n".join(code_buffer))
                continue

            if in_code:
                code_buffer.append(line)
                continue

            # TITRES
            if line.startswith("# "):
                self._add_title(line[2:], 22)

            elif line.startswith("## "):
                self._add_title(line[3:], 18)

            elif line.startswith("### "):
                self._add_title(line[4:], 16)

            # LISTES
            elif line.startswith("- "):
                self._add_text("• " + line[2:])

            # PARAGRAPHE
            elif line.strip():
                self._add_text(line)

            else:
                self._add_spacing()

    def _add_title(self, text, size):
        label = ctk.CTkLabel(
            self,
            text=text,
            font=ctk.CTkFont(size=size, weight="bold"),
            anchor="w"
        )
        label.pack(fill="x", padx=10, pady=(10, 5))

    def _add_text(self, text):
        text = re.sub(r"`([^`]*)`", r"[\1]", text)

        label = ctk.CTkLabel(
            self,
            text=text,
            wraplength=800,
            justify="left",
            anchor="w"
        )
        label.pack(fill="x", padx=10, pady=2)

    def _add_code(self, code):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=10, pady=5)

        label = ctk.CTkLabel(
            frame,
            text=code,
            justify="left",
            anchor="w",
            font=ctk.CTkFont(family="Courier", size=12)
        )
        label.pack(fill="x", padx=10, pady=5)

    def _add_spacing(self):
        ctk.CTkLabel(self, text="").pack(pady=3)


# =========================================================
# TUTORIAL TAB
# =========================================================
class TutorialTabV2:
    def __init__(self, parent, app):
        self.app = app
        self.parent = parent

        self.container = ctk.CTkFrame(parent)
        self.container.pack(fill="both", expand=True)

        self.load_tutorial()

    def load_tutorial(self):
        tutorial_file = TUTORIAL_DIR / f"tutorial_{self.app.current_language}.md"

        if not tutorial_file.exists():
            tutorial_file = TUTORIAL_DIR / "tutorial_en.md"

        if not tutorial_file.exists():
            self._show_placeholder()
            return

        with open(tutorial_file, "r", encoding="utf-8") as f:
            md_content = f.read()

        MarkdownViewer(self.container, md_content)

    def _show_placeholder(self):
        label = ctk.CTkLabel(
            self.container,
            text="📚 " + get_text("no_tutorial_available", self.app.current_language),
            font=ctk.CTkFont(size=16)
        )
        label.pack(pady=50)