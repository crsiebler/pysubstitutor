from abc import ABC, abstractmethod
from typing import List
from pysubstitutor.models.text_substitution import TextSubstitution


class FormatHandler(ABC):
    """
    Base class for handling specific file formats.
    """

    @abstractmethod
    def read(self, file_path: str) -> List[TextSubstitution]:
        """
        Reads data from a file and returns a list of TextSubstitution objects.
        :param file_path: Path to the input file.
        """
        pass

    @abstractmethod
    def export(self, file_path: str, entries: List[TextSubstitution]):
        """
        Exports a list of TextSubstitution objects to a file.
        :param file_path: Path to the output file.
        :param entries: List of TextSubstitution objects to export.
        """
        pass
