import dataclasses

import pytest

from idioms.data_classes import Point, ShoppingBasket, moved


def test_dataclasses_write_init_repr_and_eq():
    assert Point(1, 2) == Point(1, 2)
    assert repr(Point(1, 2)) == "Point(x=1, y=2)"


def test_frozen_instances_cannot_be_changed():
    p = Point(0, 0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.x = 5


def test_replace_makes_a_new_copy():
    p = Point(0, 0)
    assert moved(p, 3, 4) == Point(3, 4)
    assert p == Point(0, 0)
    assert p.distance_to(moved(p, 3, 4)) == 5


def test_each_basket_gets_its_own_list():
    a, b = ShoppingBasket("ada"), ShoppingBasket("bob")
    a.add("tea")
    assert a.items == ["tea"]
    assert b.items == []


def test_frozen_dataclasses_can_be_dict_keys():
    visits = {Point(0, 0): "home"}
    assert visits[Point(0, 0)] == "home"
