"""f-strings (PEP 498, Python 3.6), and the ``=`` specifier for debugging (Python 3.8).

Put an expression inside ``{}`` and it is evaluated in place. After a colon comes a format spec:
width, alignment, decimal places, thousands separators.
"""


def receipt_line(item: str, price: float) -> str:
    return f"{item:<10}{price:>8.2f}"


def big_number(n: int) -> str:
    return f"{n:,}"


def percent(part: int, whole: int) -> str:
    return f"{part / whole:.1%}"


def debug(total: int) -> str:
    """``{total=}`` prints the expression as well as its value."""
    return f"{total=}"
