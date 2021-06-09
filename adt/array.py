"""Array abstract data types."""

import ctypes
from collections import namedtuple
from typing import Any, Iterator, Tuple


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

    def capacity(self) -> int:
        """Return the array's capacity.

        >>> Array(20).capacity()
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

    def __getitem__(self, index) -> Any:
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError(f"Index out of range: {index}")

    def __setitem__(self, index, value) -> None:
        if 0 <= index < self._size:
            self._data[index] = value
        else:
            raise IndexError(f"Index out of range: {index}")

    def __iter__(self):
        yield from self._data

    def __str__(self) -> str:
        return f"Array{(*self._data,)}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self._size})"


class Array2D:
    Capacity = namedtuple("Capacity", "rows columns items")
    Data = namedtuple("Data", "row column data")

    def __init__(self, rows: int, cols: int) -> None:
        self._table = self.Capacity(rows, cols, rows * cols)
        self._data = [(ctypes.py_object * cols)() for _ in range(rows)]
        self.clear()

    def rows(self) -> int:
        return self._table.rows

    def columns(self) -> int:
        return self._table.columns

    def clear(self) -> None:
        for row in range(self._table.rows):
            for col in range(self._table.columns):
                self[row, col] = None

    def __iter__(self) -> Iterator["Data"]:
        for row in range(self._table.rows):
            for col in range(self._table.columns):
                yield self.Data(row, col, self[row, col])

    def capacity(self) -> "Capacity":
        return self._table

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n\t"
            + "\n\t".join(str(list(row)) for row in self._data)
            + "\n)"
        )

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = self._validate_indices(index)
        return self._data[row][col]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = self._validate_indices(index)
        self._data[row][col] = value

    def _validate_indices(self, index: Tuple[int, int]) -> Tuple[int, int]:
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError("Invalid number of indices")
        row, col = index
        if not 0 <= row < self._table.rows:
            raise IndexError("Row index out of range")
        if not 0 <= col < self._table.columns:
            raise IndexError("Column index out of range")
        return index

    def __len__(self) -> int:
        return self._table.items


class Array2DList:
    Capacity = namedtuple("Capacity", "rows columns items")

    def __init__(self, rows: int, cols: int) -> None:
        self._table = self.Capacity(rows, cols, rows * cols)
        self._data = [[None] * cols for _ in range(rows)]

    @property
    def rows(self) -> int:
        return self._table.rows

    @property
    def columns(self) -> int:
        return self._table.columns

    def clear(self) -> None:
        for row in range(self._table.rows):
            for col in range(self._table.columns):
                self[row, col] = None

    def capacity(self) -> "Capacity":
        return self._table

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n\t"
            + "\n\t".join(str(row) for row in self._data)
            + "\n)"
        )

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = self._validate_indices(index)
        return self._data[row][col]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = self._validate_indices(index)
        self._data[row][col] = value

    def _validate_indices(self, index: Tuple[int, int]) -> Tuple[int, int]:
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError("Invalid number of indices")
        row, col = index
        if not 0 <= row < self._table.rows:
            raise IndexError("Row index out of range")
        if not 0 <= col < self._table.columns:
            raise IndexError("Column index out of range")
        return index
