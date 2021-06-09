"""Test bag.py."""

from collections import Counter
from contextlib import redirect_stdout
from io import StringIO

import pytest
from adt.bag import Bag


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


def test_build_args():
    a = Bag("abcde", 3, [2, 4, 5], 6)
    len(a) == 4


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


def test_remove(get_hello_bag):
    with pytest.raises(ValueError):
        get_hello_bag.remove("missing")


def test_as_counter(get_hello_bag):
    assert get_hello_bag.as_counter() == Counter(
        {"e": 1, "h": 1, "l": 2, "o": 1}
    )


def test_randpop(get_hello_bag):
    assert get_hello_bag.randpop() in "hello"


def test_reversed(get_hello_bag):
    assert list(reversed(get_hello_bag)) == ["o", "l", "l", "e", "h"]
