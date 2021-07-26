"""Matrix abstract data type."""

from operator import add, sub
from typing import Any, Callable, List, NamedTuple, Tuple

from pyadt.utils import validate_index


class Size(NamedTuple):
    rows: int
    cols: int


class Matrix:
    """Build a matrix of numbers as an m × n rectangular grid."""

    def __init__(self, rows: int, cols: int, default: int = 0) -> None:
        self._rows = rows
        self._cols = cols
        self._data = [[default] * cols for _ in range(rows)]

    @property
    def rows(self) -> int:
        """Return the number of rows.

        >>> m = Matrix(4, 3)
        >>> m.rows
        4
        >>> m.rows = 5
        Traceback (most recent call last):
        AttributeError: can't set 'rows'
        """
        return self._rows

    @rows.setter
    def rows(self, value: int) -> None:
        """Raise AttributeError on rows assignment."""
        raise AttributeError("can't set 'rows'")

    @property
    def cols(self) -> int:
        """Return the number of columns.

        >>> m = Matrix(4, 3)
        >>> m.cols
        3
        >>> m.cols = 5
        Traceback (most recent call last):
        AttributeError: can't set 'cols'
        """
        return self._cols

    @cols.setter
    def cols(self, value: int) -> None:
        """Raise AttributeError on cols assignment."""
        raise AttributeError("can't set 'cols'")

    @property
    def size(self) -> Size:
        """Return the size of the matrix as a tuple (rows, cols).

        >>> m = Matrix(4, 3)
        >>> m.size
        Size(rows=4, cols=3)
        """
        return Size(self.rows, self.cols)

    @size.setter
    def size(self, value: Tuple[int, int]) -> None:
        """Raise AttributeError on cols assignment."""
        raise AttributeError("can't set 'size'")

    def scale_by(self, scalar: int) -> None:
        """Scale the matrix by an scalar.

        >>> m = Matrix(2, 2, 1)
        >>> print(m)
        Matrix([1, 1] [1, 1])
        >>> m.scale_by(3)
        >>> print(m)
        Matrix([3, 3] [3, 3])
        """
        for i, row in enumerate(self._data):
            for j, _ in enumerate(row):
                self[i, j] *= scalar

    def transpose(self) -> "Matrix":
        """Return the transposed version of the current matrix.

        >>> m = Matrix.from_list_of_lists([[1, 2, 3], [3, 4, 5]])
        >>> print(m)
        Matrix([1, 2, 3] [3, 4, 5])
        >>> t = m.transpose()
        >>> print(t)
        Matrix([1, 3] [2, 4] [3, 5])
        """
        transposed = type(self)(self.cols, self.rows)
        transposed._data = [list(row) for row in zip(*self._data)]
        return transposed

    def add(self, other: "Matrix") -> "Matrix":
        """Return the addition of matrix and other.

        >>> m = Matrix(3, 3, 10)
        >>> print(m)
        Matrix([10, 10, 10] [10, 10, 10] [10, 10, 10])
        >>> n = m.add(Matrix(3, 3, 2))
        >>> print(n)
        Matrix([12, 12, 12] [12, 12, 12] [12, 12, 12])
        """
        return self.__add__(other)

    def __add__(self, other: "Matrix") -> "Matrix":
        return self._compute(other, operation=add)

    def _compute(self, other: "Matrix", operation: Callable):
        if not (other.__class__ is self.__class__):
            raise TypeError("matrix object expected")

        if other.size == self.size:
            matrix = type(self)(self._rows, self._cols)
            for i, row in enumerate(self._data):
                for j, _ in enumerate(row):
                    matrix[i, j] = operation(self[i, j], other[i, j])
            return matrix

        raise ValueError("invalid matrix size")

    def subtract(self, other: "Matrix") -> "Matrix":
        """Return the subtraction of matrix and other.

        >>> m = Matrix(3, 3, 10)
        >>> print(m)
        Matrix([10, 10, 10] [10, 10, 10] [10, 10, 10])
        >>> n = m.subtract(Matrix(3, 3, 2))
        >>> print(n)
        Matrix([8, 8, 8] [8, 8, 8] [8, 8, 8])
        """
        return self.__sub__(other)

    def __sub__(self, other: "Matrix") -> "Matrix":
        return self._compute(other, operation=sub)

    def multiply(self, other: "Matrix") -> "Matrix":
        """Return the multiplication of matrix and other.

        >>> m = Matrix.from_list_of_lists([[0, 1], [2, 3], [4, 5]])
        >>> print(m)
        Matrix([0, 1] [2, 3] [4, 5])
        >>> n = Matrix.from_list_of_lists([[6, 7, 8], [9, 1, 0]])
        >>> print(n)
        Matrix([6, 7, 8] [9, 1, 0])
        >>> r = m.multiply(n)
        >>> print(r)
        Matrix([9, 1, 0] [39, 17, 16] [69, 33, 32])
        """
        return self.__mul__(other)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if not (other.__class__ is self.__class__):
            raise TypeError("matrix object expected")
        if self.cols != other.rows:
            raise ValueError("invalid matrix size")

        matrix = type(self)(self.rows, other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.rows):
                    matrix[i, j] += self[i, k] * other[k, j]

        return matrix

    @classmethod
    def from_list_of_lists(cls, iterable: List[List[Any]], /) -> "Matrix":
        """Return a new matrix built from a list of lists.

        >>> m = Matrix.from_list_of_lists([[1, 2], [3, 4], [5, 6]])
        >>> print(m)
        Matrix([1, 2] [3, 4] [5, 6])
        """
        if len(set(len(row) for row in iterable)) > 1:
            raise ValueError("invalid matrix size")

        matrix = cls(rows=len(iterable), cols=len(iterable[0]))

        for i, rows in enumerate(iterable):
            for j, value in enumerate(rows):
                matrix[i, j] = value

        return matrix

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = validate_index(index, self.rows, self.cols)
        return self._data[row][col]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = validate_index(index, self.rows, self.cols)
        self._data[row][col] = value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(rows={self._rows}, cols={self._cols})"
        )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({' '.join(str(row) for row in self._data)})"
        )
