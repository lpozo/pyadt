import ctypes
from collections import namedtuple
from typing import Any, Iterator, Tuple


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
