"""Structural pattern matching: ``match`` and ``case`` (PEP 634, Python 3.10).

``match`` is not only a switch on values. A case can check the shape of the data (a list of two
items, a dict with a "type" key, an instance with given attributes) and pull values out of it.
"""

from dataclasses import dataclass


@dataclass
class Click:
    x: int
    y: int


@dataclass
class KeyPress:
    key: str


def handle_command(command: str) -> str:
    match command.split():
        case ["go", direction]:
            return f"going {direction}"
        case ["take", *items] if items:
            return "taking " + " and ".join(items)
        case ["quit" | "exit"]:
            return "bye"
        case _:
            return "unknown command"


def handle_event(event) -> str:
    match event:
        case Click(x=0, y=0):
            return "click at the origin"
        case Click(x=x, y=y):
            return f"click at {x},{y}"
        case KeyPress(key="q"):
            return "quit"
        case {"type": "scroll", "amount": int(amount)}:
            return f"scroll by {amount}"
        case _:
            return "ignored"
