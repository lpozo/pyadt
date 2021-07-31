"""Test bag.py."""

from collections import Counter
from contextlib import redirect_stdout
from io import StringIO

import pytest

from pyadt import Bag


@pytest.fixture
def get_hello_bag():
    return Bag("hello")


@pytest.mark.parametrize(
    "iterable, expected",
    [
        pytest.param([2, 4, 5, 6], 4),  # List
        pytest.param((2, 4, 5, 6), 4),  # Tuple
        pytest.param({2, 4, 5, 6}, 4),  # Set
        pytest.param("hello", 5),  # String
    ],
)
def test_build(iterable, expected):
    b = Bag(iterable)
    assert len(b) == expected


def test_add():
    b = Bag()
    b.add(1)
    assert 1 in b
    assert len(b) == 1


def test_remove(get_hello_bag):
    with pytest.raises(ValueError):
        get_hello_bag.remove("missing")


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param("l", 2),
        pytest.param("h", 1),
        pytest.param("a", 0),
    ],
)
def test_count(get_hello_bag, value, expected):
    assert get_hello_bag.count(value) == expected


def test_clear(get_hello_bag):
    get_hello_bag.clear()
    assert len(get_hello_bag) == 0


def test_pop(get_hello_bag):
    assert get_hello_bag.pop() == "o"


def test_pop_empty():
    b = Bag()
    with pytest.raises(IndexError):
        b.pop()


def test_randpop(get_hello_bag):
    assert get_hello_bag.randpop() in "hello"


def test_randpop_empty():
    b = Bag()
    with pytest.raises(IndexError):
        b.randpop()


def test_as_counter(get_hello_bag):
    assert get_hello_bag.as_counter() == Counter(
        {"e": 1, "h": 1, "l": 2, "o": 1}
    )


def test_as_counter_unhashable():
    b = Bag([[1, 2], 3, 4])
    with pytest.raises(TypeError):
        b.as_counter()


@pytest.mark.parametrize(
    "item, expected",
    [pytest.param("h", True), pytest.param("a", False)],
)
def test_contains(item, expected, get_hello_bag):
    assert (item in get_hello_bag) == expected


def test_repr(get_hello_bag):
    string_io = StringIO()
    with redirect_stdout(string_io):
        print(get_hello_bag)
    assert (
        f"{get_hello_bag.__class__.__name__}(['h', 'e', 'l', 'l', 'o'])\n"
        in string_io.getvalue()
    )


def test_reversed(get_hello_bag):
    assert list(reversed(get_hello_bag)) == ["o", "l", "l", "e", "h"]


def test_iter(get_hello_bag):
    assert list(iter(get_hello_bag)) == ["h", "e", "l", "l", "o"]
