"""Type hints (PEP 484, Python 3.5), ``list[int]`` (PEP 585, 3.9) and ``X | None`` (PEP 604, 3.10).

Python does not check hints when the code runs. They are for readers and for tools such as mypy or
your editor, which catch the mistake before you run anything.
"""

from typing import Protocol, TypedDict


def average(values: list[float]) -> float | None:
    """The mean, or None for an empty list. The ``| None`` tells the caller to handle that case."""
    if not values:
        return None
    return sum(values) / len(values)


class Book(TypedDict):
    title: str
    year: int


def titles_before(books: list[Book], year: int) -> list[str]:
    return [book["title"] for book in books if book["year"] < year]


class HasArea(Protocol):
    """Structural typing: anything with an ``area()`` method fits, no inheritance needed."""

    def area(self) -> float: ...


def total_area(shapes: list[HasArea]) -> float:
    return sum(shape.area() for shape in shapes)
