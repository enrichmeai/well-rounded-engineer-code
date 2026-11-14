"""Generators: ``yield`` (PEP 255, Python 2.2) and ``yield from`` (PEP 380, Python 3.3).

A generator produces values one at a time, only when asked. It can describe an endless sequence,
or a huge file, without holding it all in memory.
"""

from collections.abc import Iterable, Iterator
from itertools import islice


def fibonacci() -> Iterator[int]:
    """Every Fibonacci number, for ever. Safe, because nothing is computed until it is asked for."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def first(n: int, values: Iterable[int]) -> list[int]:
    return list(islice(values, n))


def flatten(nested: Iterable) -> Iterator:
    """Yields the leaves of nested lists in order. ``yield from`` hands over to a sub-generator."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def non_blank_lines(lines: Iterable[str]) -> Iterator[str]:
    """A generator expression: like a list comprehension, but lazy."""
    return (line.strip() for line in lines if line.strip())
