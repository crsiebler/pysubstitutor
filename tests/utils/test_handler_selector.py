import pytest
from pysubstitutor.utils.handler_selector import get_handler_by_extension
from pysubstitutor.handlers.plist_handler import PlistHandler
from pysubstitutor.handlers.gboard_handler import GboardHandler
from pysubstitutor.handlers.markdown_handler import MarkdownHandler


def test_get_handler_by_extension_read():
    """
    Tests get_handler_by_extension for read mode.
    """
    assert isinstance(get_handler_by_extension("file.plist", "read"), PlistHandler)
    assert isinstance(get_handler_by_extension("file.gboard", "read"), GboardHandler)
    assert isinstance(get_handler_by_extension("file.md", "read"), MarkdownHandler)


def test_get_handler_by_extension_export():
    """
    Tests get_handler_by_extension for export mode.
    """
    assert isinstance(get_handler_by_extension("file.plist", "export"), PlistHandler)
    assert isinstance(get_handler_by_extension("file.gboard", "export"), GboardHandler)
    assert isinstance(get_handler_by_extension("file.md", "export"), MarkdownHandler)


def test_get_handler_by_extension_invalid_extension():
    """
    Tests get_handler_by_extension with an invalid file extension.
    """
    with pytest.raises(ValueError, match="Unsupported file extension: .unknown"):
        get_handler_by_extension("file.unknown", "read")


def test_get_handler_by_extension_invalid_mode():
    """
    Tests get_handler_by_extension with an invalid mode.
    """
    with pytest.raises(ValueError, match="Unsupported mode: invalid"):
        get_handler_by_extension("file.plist", "invalid")
