import csv
from typing import List
from pysubstitutor.models.text_substitution import TextSubstitution
from .format_handler import FormatHandler


class GboardHandler(FormatHandler):
    def read(self, file_path: str) -> List[TextSubstitution]:
        raise NotImplementedError("Gboard read is not implemented.")

    def export(self, file_path: str, entries: List[TextSubstitution]):
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            file.write("# Gboard Dictionary version:1\n\n")
            writer = csv.writer(file, delimiter="\t")
            for entry in entries:
                writer.writerow([entry.shortcut.strip(), entry.phrase.strip(), "en-US"])
