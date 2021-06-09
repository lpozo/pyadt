"""Queue abstract data type."""

from collections import deque
from typing import Any, Iterable, Iterator, Optional


class Queue:
    """Implement a Queue (FIFO) abstract data type.

    >>> Queue()
    Queue([])
    >>> q = Queue([1, 2, 3])
    >>> q
    Queue([1, 2, 3])
    >>> len(q)
    3
    >>> 1 in q
    True
    >>> 10 in q
    False
    >>> for item in reversed(q):
    ...     print(item)
    3
    2
    1
    """

    def __init__(
        self, iterable: Optional[Iterable[Any]] = None, /, *args
    ) -> None:
        self._data: deque = deque()
        if iterable is not None:
            try:
                self._data.extend(iterable)
            except TypeError:
                self._data.extend([iterable])
        self._data.extend(args)

    def enqueue(self, item: Any) -> None:
        """Add items to the right end of the queue.

        >>> numbers = Queue()
        >>> for number in range(1, 5):
        ...     numbers.enqueue(number)
        >>> numbers
        Queue([1, 2, 3, 4])
        """
        self._data.append(item)

    def dequeue(self) -> Any:
        """Remove and return an item from the left end of the queue.

        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> q
        Queue([1, 2, 3])
        >>> for i in range(len(q)):
        ...     q.dequeue()
        1
        2
        3
        >>> q
        Queue([])
        >>> q.dequeue()
        Traceback (most recent call last):
        IndexError: dequeue from an empty queue
        """
        try:
            return self._data.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None

    def remove(self, item: Any) -> None:
        """Remove the first occurrence of item.

        >>> q = Queue(1, 2, 3)
        >>> q.remove(2)
        >>> q
        Queue([1, 3])
        >>> q.remove(10)
        Traceback (most recent call last):
        ValueError: Queue.remove(x): x not found
        """
        try:
            self._data.remove(item)
        except ValueError:
            raise ValueError(
                f"{self.__class__.__name__}.remove(x): x not found"
            ) from None

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self._data)})"

    def __iter__(self) -> Iterator:
        yield from self._data

    def __reversed__(self) -> Iterator:
        yield from reversed(self._data)
