"""Test set.py."""

from typing import OrderedDict
import pytest

from pyadt import Map


@pytest.mark.parametrize(
    "iterable, expected",
    [
        pytest.param({}, 0),  # Empty dict
        pytest.param({"one": 1, "two": 2}, 2),  # dict
        pytest.param(OrderedDict({"one": 1, "two": 2}), 2),
    ],
)
def test_build(iterable, expected):
    m = Map(iterable)
    assert len(m) == expected


def test_build_kwargs():
    m = Map(one=1, two=2)
    assert len(m) == 2


def test_build_unhashable():
    m = Map()
    with pytest.raises(TypeError, match="unhashable type: 'list'"):
        m[[1, 2]] = 12


@pytest.fixture
def mock_map():
    return Map(one=1, two=2, three=3)


def test_keys(mock_map):
    assert list(mock_map.keys()) == ["one", "two", "three"]
    assert list(mock_map) == ["one", "two", "three"]


def test_values(mock_map):
    assert list(mock_map.values()) == [1, 2, 3]


def test_items(mock_map):
    assert list(mock_map.items()) == [("one", 1), ("two", 2), ("three", 3)]


def test_update(mock_map):
    assert mock_map["one"] == 1
    assert mock_map["two"] == 2
    mock_map.update(one=11, two=22, four=4)
    assert mock_map["one"] == 11
    assert mock_map["two"] == 22
    assert mock_map["four"] == 4


def test_set_default():
    m = Map()
    d = m.set_default("one", 1)
    assert m["one"] == 1
    assert d == 1
    m["two"] = 2
    d = m.set_default("two", 22)
    assert m["two"] == 2
    assert d == 2


def test_pop(mock_map):
    assert mock_map.pop("one") == 1
    assert "one" not in mock_map
    with pytest.raises(KeyError):
        mock_map.pop("missing")


def test_popitem(mock_map):
    assert mock_map.popitem() == ("three", 3)
    mock_map.popitem()
    mock_map.popitem()
    with pytest.raises(KeyError, match="popitem from empty Map"):
        mock_map.popitem()


def test_clear(mock_map):
    assert len(mock_map) == 3
    mock_map.clear()
    assert len(mock_map) == 0


def test_fromkeys():
    m = Map.fromkeys(["one", "two"])
    assert m["one"] is None
    assert m["two"] is None
    assert len(m) == 2
    n = Map.fromkeys(("cats", "dogs"), 0)
    assert sum(n.values()) == 0


def test_del(mock_map):
    del mock_map["one"]
    assert "one" not in mock_map
