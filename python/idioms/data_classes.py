"""Dataclasses (Python 3.7, PEP 557). ``slots=True`` and ``kw_only=True`` arrived in 3.10.

A dataclass writes ``__init__``, ``__repr__`` and ``__eq__`` from the fields you declare.
``frozen=True`` makes instances read-only, which makes them safe to share and to use as dict keys.
"""

from dataclasses import dataclass, field, replace


@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass
class ShoppingBasket:
    owner: str
    # A mutable default must come from a factory, or every basket would share one list.
    items: list[str] = field(default_factory=list)

    def add(self, item: str) -> None:
        self.items.append(item)


def moved(point: Point, dx: float, dy: float) -> Point:
    """A frozen dataclass is changed by making a new copy with ``replace``."""
    return replace(point, x=point.x + dx, y=point.y + dy)
