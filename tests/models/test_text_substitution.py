from pysubstitutor.models.text_substitution import TextSubstitution


def test_text_substitution_equality():
    """
    Tests the equality of TextSubstitution objects.
    """
    ts1 = TextSubstitution(shortcut="smile", phrase="😊")
    ts2 = TextSubstitution(shortcut="smile", phrase="😊")
    ts3 = TextSubstitution(shortcut="shrug", phrase="¯\\_(ツ)_/¯")

    assert ts1 == ts2
    assert ts1 != ts3


def test_text_substitution_representation():
    """
    Tests the string representation of TextSubstitution objects.
    """
    ts = TextSubstitution(shortcut="smile", phrase="😊")
    assert str(ts) == "TextSubstitution(shortcut='smile', phrase='😊')"
