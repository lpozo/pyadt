from collections import deque
from typing import Any, Iterator


class Queue:
    """Create a queue abstract data type.

    >>> Queue()
    Queue([])
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.enqueue(3)
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

    def __init__(self) -> None:
        self._items = deque()

    def enqueue(self, item: Any) -> None:
        """Add items to the right end of the queue.

        >>> numbers = Queue()
        >>> for number in range(1, 5):
        ...     numbers.enqueue(number)
        >>> numbers
        Queue([1, 2, 3, 4])
        """
        self._items.append(item)

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
        IndexError: Empty queue
        """
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("Empty queue") from None

    def remove(self, item: Any) -> None:
        """Remove the first occurrence of item.

        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> q.remove(2)
        >>> q
        Queue([1, 3])
        >>> q.remove(10)
        Traceback (most recent call last):
        ValueError: Queue.remove(x): x not found
        """
        try:
            self._items.remove(item)
        except ValueError:
            raise ValueError(
                f"{self.__class__.__name__}.remove(x): x not found"
            ) from None

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self._items)})"

    def __iter__(self) -> Iterator:
        yield from self._items

    def __reversed__(self) -> Iterator:
        yield from reversed(self._items)


if __name__ == "__main__":
    # Tests
    numbers = Queue()
    print(numbers)

    # Enqueue items
    for number in range(1, 5):
        numbers.enqueue(number)
        print(numbers)

    # Support len()
    print(f"Length: {len(numbers)}")

    # Support membership
    print("2 in numbers", "->", 2 in numbers)
    print("10 in numbers", "->", 10 in numbers)

    # Support iteration
    print("Normal iteration")
    for number in numbers:
        print(f"Number: {number}")

    print("Reverse iteration")
    for number in reversed(numbers):
        print(f"Number: {number}")

    # Dequeue items
    for i in range(len(numbers)):
        numbers.dequeue()
        print(numbers)
