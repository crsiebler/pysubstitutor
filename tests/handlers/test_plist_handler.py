import io

from pysubstitutor.handlers.plist_handler import PlistHandler
from pysubstitutor.models.text_substitution import TextSubstitution


def test_plist_handler_read():
    """
    Tests the PlistHandler's read method with valid plist data.
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
    </array>
    </plist>"""
    handler = PlistHandler()
    input_stream = io.BytesIO(plist_data.encode("utf-8"))  # Explicitly encode as UTF-8
    entries = handler.read(input_stream)

    assert len(entries) == 1
    assert entries[0] == TextSubstitution(shortcut="smile", phrase="😊")
