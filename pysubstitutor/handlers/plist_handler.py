import plistlib
import html
import re
from typing import List
from pysubstitutor.models.text_substitution import TextSubstitution
from .format_handler import FormatHandler


class PlistHandler(FormatHandler):
    def read(self, file_path: str) -> List[TextSubstitution]:
        with open(file_path, "rb") as file:
            plist_data = plistlib.load(file)

            if isinstance(plist_data, list):
                raw_entries = plist_data
            elif isinstance(plist_data, dict):
                raw_entries = plist_data.get("NSUserDictionaryReplacementItems", [])
            else:
                raise ValueError("Unsupported plist format: Expected a dict or list.")

            return [
                TextSubstitution(
                    shortcut=html.unescape(entry.get("shortcut", "").strip()),
                    phrase=html.unescape(
                        re.sub(
                            r"\s+",
                            " ",
                            entry.get("phrase", "").replace("\n", "").strip(),
                        )
                    ),
                )
                for entry in raw_entries
                if isinstance(entry, dict)
                and entry.get("shortcut")
                and entry.get("phrase")
            ]

    def export(self, file_path: str, entries: List[TextSubstitution]):
        raise NotImplementedError("Plist export is not implemented.")
