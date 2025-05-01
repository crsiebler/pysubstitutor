from typing import List
from pysubstitutor.models.text_substitution import TextSubstitution
from .format_handler import FormatHandler


class MarkdownHandler(FormatHandler):
    def read(self, file_path: str) -> List[TextSubstitution]:
        raise NotImplementedError("Markdown read is not implemented.")

    def export(self, file_path: str, entries: List[TextSubstitution]):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("| Shortcut | Phrase |\n")
            file.write("|:--|:--|\n")
            for entry in entries:
                file.write(f"| {entry.shortcut} | {entry.phrase} |\n")
