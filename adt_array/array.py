"""Array abstract data type based on ctypes.py_object."""

import ctypes
from typing import Any


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
