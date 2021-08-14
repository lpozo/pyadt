"""Test set.py."""

import pytest

from pyadt import Set


@pytest.mark.parametrize(
    "iterable, expected",
    [
        pytest.param([], 0),  # List
        pytest.param([2, 4, 5, 6], 4),  # List
        pytest.param((2, 4, 5, 5, 5, 6), 4),  # Tuple
        pytest.param({2, 4, 5, 6, 2, 2}, 4),  # Set
        pytest.param("hello", 4),  # String
    ],
)
def test_build(iterable, expected):
    s = Set(iterable)
    assert len(s) == expected


def test_build_unhashable():
    with pytest.raises(TypeError):
        Set([[1, 2], 2, {"one": 1}])


def test_add():
    s = Set()
    s.add(1)
    assert 1 in s
    s.add(1)
    assert len(s) == 1


def test_remove():
    s = Set([1, 2])
    s.remove(1)
    assert 1 not in s
    s.remove(2)
    assert 2 not in s
    assert len(s) == 0


def test_remove_missing():
    s = Set([1, 2])
    with pytest.raises(KeyError, match="42 not in set"):
        s.remove(42)


def test_discard():
    s = Set([1, 2])
    s.discard(1)
    assert 1 not in s
    s.discard(42)
    assert len(s) == 1


def test_pop():
    s = Set([1, 2])
    assert s.pop() == 2
    assert len(s) == 1


def test_pop_empty():
    s = Set([])
    with pytest.raises(KeyError, match="pop from an empty set"):
        s.pop()


def test_clear():
    s = Set([1, 2, 3])
    assert len(s) == 3
    s.clear()
    assert len(s) == 0


def test_update():
    s = Set([1, 2, 3])
    o = Set([4, 5, 6])
    s.update(o)
    assert len(s) == 6
    assert 4 in s
    assert 5 in s
    assert 6 in s


def test_is_subset():
    s = Set([1, 2, 3])
    o = Set([1, 2, 3, 4, 5])
    assert s.is_subset(o)
    assert not o.is_subset(s)


def test_is_suerset():
    s = Set([1, 2, 3])
    o = Set([1, 2, 3, 4, 5])
    assert o.is_superset(s)
    assert not s.is_superset(o)


def test_is_disjoint():
    s = Set([1, 2, 3])
    o = Set([4, 5, 6])
    assert s.is_disjoint(o)
    a = Set([2, 4, 6])
    assert not s.is_disjoint(a)


def test_union():
    s = Set([1, 2])
    o = Set([1, 4])
    n = s.union(o)
    assert len(n) == 3
    assert 4 in n


def test_intersection():
    s = Set([1, 2, 3])
    o = Set([2, 4, 3, 6])
    n = s.intersection(o)
    assert len(n) == 2
    assert 2 in n
    assert 3 in n


def test_difference():
    s = Set([1, 2, 3])
    o = Set([2, 4, 3, 6])
    n = s.difference(o)
    assert len(n) == 1
    assert 1 in n


def test_equal():
    s = Set([1, 2, 3])
    o = Set([2, 1, 3])
    n = Set([4, 1, 2])
    assert s == o
    assert n != o
