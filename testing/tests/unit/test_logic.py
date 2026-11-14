"""Unit tests: the rule on its own, no server, no browser. Fast, so there are many of them."""

from decimal import Decimal

import pytest

from tipsplit.logic import split_bill


def test_splits_evenly_with_a_tip():
    split = split_bill("60", "3", "10")
    assert split.tip == Decimal("6.00")
    assert split.total == Decimal("66.00")
    assert split.per_person == Decimal("22.00")


def test_each_share_is_rounded_up_so_the_bill_is_covered():
    split = split_bill("10", "3")
    assert split.per_person == Decimal("3.34")
    assert split.per_person * 3 >= split.total


def test_no_tip_by_default():
    assert split_bill("20", "2").tip == Decimal("0.00")


@pytest.mark.parametrize(
    ("total", "people", "tip", "message"),
    [
        ("abc", "2", "10", "must be numbers"),
        ("0", "2", "10", "total must be more than 0"),
        ("-5", "2", "10", "total must be more than 0"),
        ("NaN", "2", "10", "total must be more than 0"),
        ("10", "0", "10", "people"),
        ("10", "1.5", "10", "people"),
        ("10", "2", "150", "tip must be between 0 and 100"),
    ],
)
def test_rejects_bad_input(total, people, tip, message):
    with pytest.raises(ValueError, match=message):
        split_bill(total, people, tip)
