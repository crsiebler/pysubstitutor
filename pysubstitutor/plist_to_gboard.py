import csv
import html
import logging
import plistlib
import re
from typing import List

from pysubstitutor.file_converter import FileConverterInterface
from pysubstitutor.text_substitution import TextSubstitution


class AppleToGboardConverter(FileConverterInterface):
    """
    A file converter that converts Apple text substitution plist files
    to Gboard dictionary files in TSV format.
    """

    def __init__(self, logger=None):
        self.entries: List[TextSubstitution] = []
        self.logger = logger or logging.getLogger(__name__)

    def read_file(self, input_file: str):
        """
        Reads data from an Apple text substitution plist file.
        :param input_file: Path to the input plist file.
        """
        self.logger.info(f"Reading input file: {input_file}")
        try:
            with open(input_file, "rb") as file:
                plist_data = plistlib.load(file)

                # Handle top-level array or dictionary
                if isinstance(plist_data, list):
                    self.logger.debug("plist_data is a list.")
                    self.logger.info(f"plist_data contains {len(plist_data)} items.")
                    raw_entries = plist_data  # Top-level array
                elif isinstance(plist_data, dict):
                    self.logger.debug("plist_data is a dict.")
                    raw_entries = plist_data.get("NSUserDictionaryReplacementItems", [])
                    self.logger.info(
                        f"plist_data contains {len(raw_entries)} items in 'NSUserDictionaryReplacementItems'."
                    )
                else:
                    self.logger.error(
                        "Unsupported plist format: Expected a dict or list."
                    )
                    raise ValueError(
                        "Unsupported plist format: Expected a dict or list."
                    )

                self.entries = [
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
                self.logger.info(
                    f"Loaded {len(self.entries)} entries from the input file."
                )
        except Exception as e:
            self.logger.error(f"Failed to read the input file: {e}")
            raise ValueError(f"Failed to read the input file: {e}")

    def export_file(self, output_file: str):
        """
        Exports data to a Gboard dictionary file in TSV format.
        :param output_file: Path to the output TSV file.
        """
        self.logger.info(f"Exporting data to output file: {output_file}")
        try:
            with open(output_file, "w", newline="", encoding="utf-8") as file:
                file.write("# Gboard Dictionary version:1\n\n")

                writer = csv.writer(file, delimiter="\t")
                for entry in self.entries:
                    shortcut = entry.shortcut.strip()
                    phrase = entry.phrase.strip()

                    writer.writerow([shortcut, phrase, "en-US"])
                self.logger.info(
                    f"Exported {len(self.entries)} entries to the output file."
                )
        except Exception as e:
            self.logger.error(f"Failed to export the file: {e}")
            raise ValueError(f"Failed to export the file: {e}")
