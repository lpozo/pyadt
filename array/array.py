import ctypes
from typing import Any


class Array:
    def __init__(self, size: int) -> None:
        self._size = size
        self._data = (ctypes.py_object * self._size)()
        self.clear()

    def __len__(self) -> int:
        return len(self._data)

    def capacity(self) -> int:
        return self._size

    def clear(self) -> None:
        for i in range(self._size):
            self._data[i] = None

    def __getitem__(self, index) -> Any:
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError(f"Index out of range: {index}")

    def __setitem__(self, index, value):
        if 0 <= index < self._size:
            self._data[index] = value
        raise IndexError(f"Index out of range: {index}")

    def __iter__(self):
        yield from self._data

    def __str__(self) -> str:
        return f"Array{(*self._data,)}"
