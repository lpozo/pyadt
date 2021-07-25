"""Test array.py."""

import pytest

from pyadt import Array


def test_build():
    a = Array(5)
    assert len(a) == 5


def test_assignment():
    a = Array(5)
    with pytest.raises(IndexError):
        a[10] = 42


def test_clear():
    a = Array(5)
    for i in range(len(a)):
        a[i] = 1
    assert sum(a) == 5
    a.clear()
    assert not any(a)


def test_reversed():
    a = Array(5)
    for i in range(len(a)):
        a[i] = i
    assert list(reversed(a)) == [4, 3, 2, 1, 0]
