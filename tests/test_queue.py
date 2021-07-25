"""Test queue.py."""

from contextlib import redirect_stdout
from io import StringIO

import pytest
from pyadt import Queue


@pytest.fixture
def get_hello_queue():
    return Queue("hello")


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
    b = Queue(iterable)
    assert len(b) == expected


def test_enqueue():
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    assert len(q) == 10


def test_dequeue(get_hello_queue):
    for _ in range(len(get_hello_queue)):
        get_hello_queue.dequeue()
    assert len(get_hello_queue) == 0


def test_front(get_hello_queue):
    assert get_hello_queue.front() == "h"


def test_front_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.front()


def test_dequeue_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_remove(get_hello_queue):
    get_hello_queue.remove("h")
    assert not ("h" in get_hello_queue)


def test_remove_missing(get_hello_queue):
    with pytest.raises(ValueError):
        get_hello_queue.remove("a")


@pytest.mark.parametrize(
    "item, expected",
    [pytest.param("h", True), pytest.param("a", False)],
)
def test_contains(item, expected, get_hello_queue):
    assert (item in get_hello_queue) == expected


def test_repr(get_hello_queue):
    string_io = StringIO()
    with redirect_stdout(string_io):
        print(get_hello_queue)
    assert (
        f"{get_hello_queue.__class__.__name__}(['h', 'e', 'l', 'l', 'o'])\n"
        in string_io.getvalue()
    )


def test_iteration(get_hello_queue):
    assert list(get_hello_queue) == ["h", "e", "l", "l", "o"]


def test_reverse_iteration(get_hello_queue):
    assert list(reversed(get_hello_queue)) == ["o", "l", "l", "e", "h"]
