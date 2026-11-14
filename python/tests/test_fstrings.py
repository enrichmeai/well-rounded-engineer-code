from idioms.fstrings import big_number, debug, percent, receipt_line


def test_width_alignment_and_decimals():
    assert receipt_line("tea", 2.5) == "tea           2.50"


def test_thousands_separator_and_percent():
    assert big_number(1234567) == "1,234,567"
    assert percent(1, 3) == "33.3%"


def test_the_equals_specifier_shows_the_name_too():
    assert debug(42) == "total=42"
