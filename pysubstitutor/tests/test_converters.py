import pytest
import plistlib
from pysubstitutor.converters.file_converter import FileConverter
from pysubstitutor.handlers.gboard_handler import GboardHandler
from pysubstitutor.handlers.plist_handler import PlistHandler
from pysubstitutor.models import TextSubstitution


@pytest.fixture
def sample_plist_file_as_list(tmp_path):
    """
    Creates a temporary plist file with a list as the top-level structure.
    """
    plist_data = [
        {"shortcut": "smile", "phrase": "😊"},
        {"shortcut": "shrug", "phrase": "¯\\_(ツ)_/¯"},
        {"shortcut": "quote", "phrase": '"To be or not to be"'},
    ]
    file_path = tmp_path / "list_based.plist"
    with open(file_path, "wb") as file:
        plistlib.dump(plist_data, file)
    return file_path


@pytest.fixture
def sample_plist_file_as_dict(tmp_path):
    """
    Creates a temporary plist file with a dictionary as the top-level structure.
    """
    plist_data = {
        "NSUserDictionaryReplacementItems": [
            {"shortcut": "smile", "phrase": "😊"},
            {"shortcut": "shrug", "phrase": "¯\\_(ツ)_/¯"},
            {"shortcut": "quote", "phrase": '"To be or not to be"'},
        ]
    }
    file_path = tmp_path / "dict_based.plist"
    with open(file_path, "wb") as file:
        plistlib.dump(plist_data, file)
    return file_path


@pytest.fixture
def expected_tsv_content():
    """
    Returns the expected TSV content for the plist files.
    """
    return (
        "# Gboard Dictionary version:1\n\n"
        "smile\t😊\ten-US\n"
        "shrug\t¯\\_(ツ)_/¯\ten-US\n"
        'quote\t"""To be or not to be"""\ten-US\n'
    )


@pytest.fixture
def sample_plist_file_with_newlines(tmp_path):
    """
    Creates a temporary plist file with phrases containing newlines.
    """
    plist_data = [
        {"shortcut": "multi", "phrase": "Line 1\nLine 2\nLine 3"},
        {"shortcut": "single", "phrase": "Single line\n"},
    ]
    file_path = tmp_path / "newlines.plist"
    with open(file_path, "wb") as file:
        plistlib.dump(plist_data, file)
    return file_path


@pytest.fixture
def sample_plist_file_with_multiple_whitespace(tmp_path):
    """
    Creates a temporary plist file with phrases containing multiple whitespace.
    """
    plist_data = [
        {"shortcut": "multi", "phrase": "Line   1   Line  2   Line 3"},
        {"shortcut": "single", "phrase": "Single    line"},
    ]
    file_path = tmp_path / "multiple_whitespace.plist"
    with open(file_path, "wb") as file:
        plistlib.dump(plist_data, file)
    return file_path


def test_read_file_with_list(sample_plist_file_as_list):
    """
    Tests the read_file method with a plist file that has a list as the top-level structure.
    """
    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    converter.read_file(str(sample_plist_file_as_list))

    assert len(converter.entries) == 3
    assert converter.entries[0] == TextSubstitution(shortcut="smile", phrase="😊")
    assert converter.entries[1] == TextSubstitution(
        shortcut="shrug", phrase="¯\\_(ツ)_/¯"
    )
    assert converter.entries[2] == TextSubstitution(
        shortcut="quote", phrase='"To be or not to be"'
    )


def test_read_file_with_dict(sample_plist_file_as_dict):
    """
    Tests the read_file method with a plist file that has a dictionary as the top-level structure.
    """
    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    converter.read_file(str(sample_plist_file_as_dict))

    assert len(converter.entries) == 3
    assert converter.entries[0] == TextSubstitution(shortcut="smile", phrase="😊")
    assert converter.entries[1] == TextSubstitution(
        shortcut="shrug", phrase="¯\\_(ツ)_/¯"
    )
    assert converter.entries[2] == TextSubstitution(
        shortcut="quote", phrase='"To be or not to be"'
    )


def test_export_file(sample_plist_file_as_list, expected_tsv_content, tmp_path):
    """
    Tests the export_file method with a plist file.
    """
    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    converter.read_file(str(sample_plist_file_as_list))

    output_file = tmp_path / "output.tsv"
    converter.export_file(str(output_file))

    with open(output_file, "r", encoding="utf-8") as file:
        content = file.read()

    assert content.strip() == expected_tsv_content.strip()


def test_read_file_with_invalid_format(tmp_path):
    """
    Tests the read_file method with an invalid plist format.
    """
    invalid_file = tmp_path / "invalid.plist"
    with open(invalid_file, "w", encoding="utf-8") as file:
        file.write("Invalid content")

    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    with pytest.raises(ValueError, match="Failed to read the input file"):
        converter.read_file(str(invalid_file))


def test_read_file_removes_newlines(sample_plist_file_with_newlines):
    """
    Tests the read_file method to ensure newlines are removed from phrases.
    """
    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    converter.read_file(str(sample_plist_file_with_newlines))

    assert len(converter.entries) == 2
    assert converter.entries[0] == TextSubstitution(
        shortcut="multi", phrase="Line 1Line 2Line 3"
    )
    assert converter.entries[1] == TextSubstitution(
        shortcut="single", phrase="Single line"
    )


def test_read_file_replaces_multiple_whitespace(
    sample_plist_file_with_multiple_whitespace,
):
    """
    Tests the read_file method to ensure multiple whitespace is replaced with a single space.
    """
    converter = FileConverter(
        read_handler=PlistHandler(), export_handler=GboardHandler()
    )
    converter.read_file(str(sample_plist_file_with_multiple_whitespace))

    assert len(converter.entries) == 2
    assert converter.entries[0] == TextSubstitution(
        shortcut="multi", phrase="Line 1 Line 2 Line 3"
    )
    assert converter.entries[1] == TextSubstitution(
        shortcut="single", phrase="Single line"
    )
