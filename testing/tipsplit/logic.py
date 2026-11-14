"""The business rule, kept apart from the web code so it can be unit tested on its own."""

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, ROUND_UP, Decimal, InvalidOperation

PENNY = Decimal("0.01")


@dataclass(frozen=True)
class Split:
    tip: Decimal
    total: Decimal
    per_person: Decimal

    def as_json(self) -> dict[str, str]:
        return {"tip": str(self.tip), "total": str(self.total), "per_person": str(self.per_person)}


def split_bill(total: str, people: str, tip_percent: str = "0") -> Split:
    """Splits a bill, tip included, between ``people``.

    Each share is rounded UP to the penny, so the group never pays less than the bill.
    Inputs are strings, exactly as they arrive from a form or a URL, and are checked here.
    """
    try:
        amount = Decimal(total)
        tip_rate = Decimal(tip_percent)
    except InvalidOperation:
        raise ValueError("total and tip must be numbers") from None
    if not people.isdigit() or int(people) < 1:
        raise ValueError("people must be a whole number of at least 1")
    if not amount.is_finite() or amount <= 0:
        raise ValueError("total must be more than 0")
    if not tip_rate.is_finite() or tip_rate < 0 or tip_rate > 100:
        raise ValueError("tip must be between 0 and 100")

    tip = (amount * tip_rate / 100).quantize(PENNY, rounding=ROUND_HALF_UP)
    grand_total = (amount + tip).quantize(PENNY)
    per_person = (grand_total / int(people)).quantize(PENNY, rounding=ROUND_UP)
    return Split(tip=tip, total=grand_total, per_person=per_person)
