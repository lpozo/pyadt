"""Array abstract data types."""

import ctypes
from typing import Any, Generator, Optional


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
        self._type = None
        self.clear()

    def clear(self, value: Optional[Any] = None) -> None:
        """Clear the array by setting all its items to value.

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
            self._data[i] = value

    def __len__(self) -> int:
        return self._size

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

    def __reversed__(self):
        yield from reversed(self._data)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}{(*self._data,)}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self._size})"
