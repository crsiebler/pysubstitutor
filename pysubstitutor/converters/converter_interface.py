from abc import ABC, abstractmethod


class ConverterInterface(ABC):
    """
    An interface for file conversion operations.
    """

    @abstractmethod
    def read_file(self, input_file: str):
        """
        Reads data from the input file.
        :param input_file: Path to the input file.
        """
        pass

    @abstractmethod
    def export_file(self, output_file: str):
        """
        Exports data to the output file.
        :param output_file: Path to the output file.
        """
        pass
