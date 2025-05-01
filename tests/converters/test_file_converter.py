import pytest
import tempfile
from pysubstitutor.converters.file_converter import FileConverter
from pysubstitutor.handlers.plist_handler import PlistHandler
from pysubstitutor.handlers.gboard_handler import GboardHandler
from pysubstitutor.models.text_substitution import TextSubstitution


@pytest.fixture
def sample_plist_file():
    """
    Provides sample plist data as a temporary file.
    """
    plist_data = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <array>
        <dict>
            <key>shortcut</key>
            <string>smile</string>
            <key>phrase</key>
            <string>😊</string>
        </dict>
        <dict>
            <key>shortcut</key>
            <string>shrug</string>
            <key>phrase</key>
            <string>¯\\_(ツ)_/¯</string>
        </dict>
    </array>
    </plist>"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".plist") as temp_file:
        temp_file.write(plist_data.encode("utf-8"))
        temp_file_path = temp_file.name
    yield temp_file_path


@pytest.fixture
def expected_gboard_output():
    """
    Provides the expected Gboard output as a string.
    """
    return (
        "# Gboard Dictionary version:1\n\n"
        "smile\t😊\ten-US\n"
        "shrug\t¯\\_(ツ)_/¯\ten-US\n"
    )


def test_file_converter_read(sample_plist_file):
    """
    Tests the FileConverter's read method with valid plist data.
    """
    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    converter.read(sample_plist_file)  # Use the read method to populate entries

    assert len(converter.entries) == 2
    assert converter.entries[0] == TextSubstitution(shortcut="smile", phrase="😊")
    assert converter.entries[1] == TextSubstitution(
        shortcut="shrug", phrase="¯\\_(ツ)_/¯"
    )


def test_file_converter_export(sample_plist_file, expected_gboard_output):
    """
    Tests the FileConverter's export method with valid data.
    """
    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    converter.read(sample_plist_file)  # Use the read method to populate entries

    with tempfile.NamedTemporaryFile(delete=False, suffix=".gboard") as temp_file:
        output_file_path = temp_file.name

    converter.export(output_file_path)  # Use the export method

    with open(output_file_path, "r", encoding="utf-8") as output_file:
        assert output_file.read() == expected_gboard_output
