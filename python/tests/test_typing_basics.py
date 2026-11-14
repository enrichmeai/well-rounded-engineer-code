import typing

from idioms.typing_basics import average, titles_before, total_area


def test_average_handles_the_empty_case():
    assert average([1.0, 2.0, 3.0]) == 2.0
    assert average([]) is None


def test_typed_dicts_are_plain_dicts_at_run_time():
    books = [{"title": "SICP", "year": 1985}, {"title": "Refactoring", "year": 1999}]
    assert titles_before(books, 1990) == ["SICP"]


def test_any_object_with_area_fits_the_protocol():
    class Square:
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side**2

    assert total_area([Square(2), Square(3)]) == 13


def test_hints_are_kept_for_tools_to_read():
    hints = typing.get_type_hints(average)
    assert hints["values"] == list[float]
    assert hints["return"] == float | None
