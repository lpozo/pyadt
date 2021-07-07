"""Array abstract data types."""

import ctypes
from collections import namedtuple
from typing import Any, Generator, Iterator, Tuple

from adt.utils import validate_index


class Array:
    """Array abstract data type based on ctypes.py_object.

    >>> a = Array(5)
    >>> a
    Array(size=5)
    >>> len(a)
    5
    >>> a[0] = 42
    >>> a[0]
    42
    >>> print(a)
    Array(42, None, None, None, None)
    """

    def __init__(self, size: int) -> None:
        self._size = size
        self._data = (ctypes.py_object * self._size)()
        self.clear()

    @property
    def capacity(self) -> int:
        """Return the array's capacity.

        >>> Array(20).capacity
        20
        """
        return self._size

    def clear(self) -> None:
        """Clear the array by setting all its items to None.

        >>> a = Array(5)
        >>> for i in range(len(a)):
        ...     a[i] = 0
        >>> print(a)
        Array(0, 0, 0, 0, 0)
        >>> a.clear()
        >>> print(a)
        Array(None, None, None, None, None)
        """
        for i in range(self._size):
            self._data[i] = None

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index: int) -> Any:
        try:
            return self._data[index]
        except IndexError:
            raise IndexError(f"Index out of range: {index}") from None

    def __setitem__(self, index: int, value: Any) -> None:
        try:
            self._data[index] = value
        except IndexError:
            raise IndexError(f"Index out of range: {index}") from None

    def __iter__(self) -> Generator[Any, None, None]:
        yield from self._data

    def __str__(self) -> str:
        return f"Array{(*self._data,)}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self._size})"


Capacity = namedtuple("Capacity", "rows cols items")
Data = namedtuple("Data", "row col data")


class Array2D:
    """2d array abstract data type based on ctypes.py_object.

    >>> a = Array2D(2, 4)
    >>> a
    Array2D(rows=2, cols=4)
    >>> a[0, 0] = 42
    """

    def __init__(self, rows: int, cols: int) -> None:
        self._table = Capacity(rows, cols, rows * cols)
        self._data = [(ctypes.py_object * cols)() for _ in range(rows)]
        self.clear()

    @property
    def rows(self) -> int:
        """Return the number of rows in the array.

        >>> a = Array2D(2, 4)
        >>> a.rows
        2
        """
        return self._table.rows

    @property
    def cols(self) -> int:
        """Return the number of columns in the array.

        >>> a = Array2D(2, 4)
        >>> a.cols
        4
        """
        return self._table.cols

    @property
    def capacity(self) -> "Capacity":
        """Return the capacity of the array.

        >>> a = Array2D(2, 4)
        >>> a.capacity
        Capacity(rows=2, cols=4, items=8)
        """
        return self._table

    def clear(self) -> None:
        """Clear the array by setting all the items to None.

        >>> a = Array2D(2, 2)
        >>> a[0, 0] = 42
        >>> a[0, 0]
        42
        >>> a.clear()
        >>> a[0, 0] is None
        True
        """
        for row in range(self._table.rows):
            for col in range(self._table.cols):
                self[row, col] = None

    def __iter__(self) -> Iterator["Data"]:
        for row in range(self._table.rows):
            for col in range(self._table.cols):
                yield Data(row, col, self[row, col])

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n\t"
            + "\n\t".join(str(list(row)) for row in self._data)
            + "\n)"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            + f"(rows={self.rows}, cols={self.cols})"
        )

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = validate_index(index, self.rows, self.cols)
        return self._data[row][col]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = validate_index(index, self.rows, self.cols)
        self._data[row][col] = value

    def __len__(self) -> int:
        return self._table.items
