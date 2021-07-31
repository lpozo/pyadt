"""Stack abstract data type."""

from collections import deque
from typing import Any, Iterator, Optional


class Stack:
    def __init__(self, iterable: Optional[Any] = None, /) -> None:
        self._data: deque = deque()
        if iterable is not None:
            self._data.extend(iterable)

    def push(self, item: Any) -> None:
        """Push an item onto the stack.

        >>> s = Stack()
        >>> s.push(42)
        >>> s
        Stack([42])
        """
        self._data.append(item)

    def pop(self) -> Any:
        """Pop an item from the top of the stack.

        >>> s = Stack([1, 2])
        >>> s.pop()
        2
        >>> s
        Stack([1])
        >>> s.pop()
        1
        >>> s
        Stack([])
        >>> s.pop()
        Traceback (most recent call last):
        IndexError: pop from an empty stack
        """
        try:
            return self._data.pop()
        except IndexError:
            raise IndexError("pop from an empty stack") from None

    def top(self) -> Any:
        """Return the item at the top of the stack.

        >>> s = Stack([1, 2, 3])
        >>> s.top()
        3
        >>> s
        Stack([1, 2, 3])
        """
        try:
            return self._data[-1]
        except IndexError:
            raise IndexError("top from an empty stack") from None

    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push(1)
        >>> s.is_empty()
        False
        """
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __contain__(self, item) -> bool:
        return item in self._data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self._data)})"

    __str__ = __repr__

    def __iter__(self) -> Iterator:
        yield from self._data

    def __reversed__(self) -> Iterator:
        yield from reversed(self._data)
