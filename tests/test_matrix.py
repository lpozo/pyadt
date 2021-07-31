"""Test matrix.py."""

from random import randint

import pytest

from pyadt import Matrix


@pytest.fixture
def mock_matrix():
    return Matrix(3, 3, 2)


def test_build(mock_matrix):
    assert mock_matrix.size == (3, 3)
    assert mock_matrix[0, 0] == 2


def test_rows(mock_matrix):
    assert mock_matrix.rows == 3


def test_rows_assign(mock_matrix):
    with pytest.raises(AttributeError):
        mock_matrix.rows = 10


def test_cols(mock_matrix):
    assert mock_matrix.cols == 3


def test_cols_assign(mock_matrix):
    with pytest.raises(AttributeError):
        mock_matrix.cols = 10


def test_size(mock_matrix):
    assert mock_matrix.size == (3, 3)


def test_size_assign(mock_matrix):
    with pytest.raises(AttributeError):
        mock_matrix.size = (5, 5)


def test_scale_by(mock_matrix):
    mock_matrix.scale_by(4)
    assert mock_matrix[randint(0, 2), randint(0, 2)] == 8


def test_transpose():
    m = Matrix.from_list_of_lists([[1, 2, 3], [3, 4, 5]])
    t = m.transpose()
    i = randint(0, 1)
    j = randint(0, 1)
    assert t.size == (3, 2)
    assert m[i, j] == t[j, i]


def test_add():
    m = Matrix(3, 3, 10)
    n = m.add(Matrix(3, 3, 2))
    assert n[randint(0, 2), randint(0, 2)] == 12
    o = m + n
    assert o[randint(0, 2), randint(0, 2)] == 22


def test_subtract():
    m = Matrix(3, 3, 10)
    n = m.subtract(Matrix(3, 3, 2))
    assert n[randint(0, 2), randint(0, 2)] == 8
    o = m - n
    assert o[randint(0, 2), randint(0, 2)] == 2


def test_multiply():
    m = Matrix(3, 3, 2)
    n = m.multiply(Matrix(3, 3, 2))
    assert n[randint(0, 2), randint(0, 2)] == 12
    o = m * Matrix(3, 3, 2)
    assert o[randint(0, 2), randint(0, 2)] == 12


def test_from_list_of_lists():
    m = Matrix.from_list_of_lists([[1, 2], [3, 4], [5, 6]])
    assert m.size == (3, 2)
