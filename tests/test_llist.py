"""Test llist.py."""

import pytest

from pyadt import LinkedList


@pytest.fixture
def mock_llist():
    return LinkedList([1, 2, 3])


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
    b = LinkedList(iterable)
    assert len(b) == expected


def test_append_left(mock_llist):
    assert len(mock_llist) == 3
    for i in range(10):
        mock_llist.append_left(i)
    assert len(mock_llist) == 13
    assert mock_llist.head.data == 9


def test_append(mock_llist):
    assert len(mock_llist) == 3
    for i in range(10):
        mock_llist.append(i)
    assert len(mock_llist) == 13
    assert mock_llist.head.data == 1


def test_insert(mock_llist):
    mock_llist.insert(1, 100)
    assert mock_llist.head.next.data == 100


def test_insert_index_error(mock_llist):
    with pytest.raises(IndexError, match="index out of range"):
        mock_llist.insert(5, 100)


def test_remove(mock_llist):
    mock_llist.remove(2)
    assert len(mock_llist) == 2
    assert mock_llist.head.next.data == 3


def test_remove_index_error(mock_llist):
    value = 100
    with pytest.raises(IndexError, match=f"{value} doesn't exist"):
        mock_llist.remove(value)


def test_reverse(mock_llist):
    mock_llist.reverse()
    assert mock_llist.head.data == 3
