"""Test queue.py."""

from contextlib import redirect_stdout
from io import StringIO

import pytest

from pyadt import Stack


@pytest.fixture
def get_hello_stack():
    return Stack("hello")


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
    s = Stack(iterable)
    assert len(s) == expected


def test_push():
    s = Stack()
    for i in range(10):
        s.push(i)
    assert len(s) == 10


def test_pop(get_hello_stack):
    for _ in range(len(get_hello_stack)):
        get_hello_stack.pop()
    assert len(get_hello_stack) == 0


def test_pop_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_top(get_hello_stack):
    assert get_hello_stack.top() == "o"


def test_top_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.top()


@pytest.mark.parametrize(
    "item, expected",
    [pytest.param("h", True), pytest.param("a", False)],
)
def test_contains(item, expected, get_hello_stack):
    assert (item in get_hello_stack) == expected


def test_repr(get_hello_stack):
    string_io = StringIO()
    with redirect_stdout(string_io):
        print(get_hello_stack)
    assert (
        f"{get_hello_stack.__class__.__name__}(['h', 'e', 'l', 'l', 'o'])\n"
        in string_io.getvalue()
    )


def test_iteration(get_hello_stack):
    assert list(get_hello_stack) == ["h", "e", "l", "l", "o"]


def test_reverse_iteration(get_hello_stack):
    assert list(reversed(get_hello_stack)) == ["o", "l", "l", "e", "h"]
