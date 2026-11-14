import pytest

from idioms.matching import Click, KeyPress, handle_command, handle_event


@pytest.mark.parametrize(
    ("command", "expected"),
    [
        ("go north", "going north"),
        ("take lamp key", "taking lamp and key"),
        ("take", "unknown command"),
        ("exit", "bye"),
        ("dance", "unknown command"),
    ],
)
def test_matches_the_shape_of_a_command(command, expected):
    assert handle_command(command) == expected


def test_matches_classes_and_dicts():
    assert handle_event(Click(0, 0)) == "click at the origin"
    assert handle_event(Click(3, 4)) == "click at 3,4"
    assert handle_event(KeyPress("q")) == "quit"
    assert handle_event({"type": "scroll", "amount": 5}) == "scroll by 5"
    assert handle_event({"type": "scroll", "amount": "lots"}) == "ignored"
