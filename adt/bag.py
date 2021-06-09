"""Bag abstract data types."""

from random import choice as _choice
from typing import Any, Counter, Iterable, List, Optional


class Bag:
    """Implement a Bag abstract data type.

    >>> b = Bag([1, 2, 3])
    >>> b
    Bag([1, 2, 3])
    >>> b.add(4)
    >>> b
    Bag([1, 2, 3, 4])
    >>> len(b)
    4
    """

    def __init__(
        self, iterable: Optional[Iterable[Any]] = None, /, *args
    ) -> None:
        self._data: List[Any] = []
        if iterable is not None:
            try:
                self._data.extend(iterable)
            except TypeError:
                self._data.extend([iterable])
        self._data.extend(args)

    def add(self, value: Any) -> None:
        """Add an object to the Bag.

        >>> b = Bag([1])
        >>> b.add(2)
        >>> b
        Bag([1, 2])
        """
        self._data.append(value)

    def remove(self, value: Any) -> None:
        """Remove an object from the Bag.

        >>> b = Bag([1, 2])
        >>> b.remove(1)
        >>> b
        Bag([2])
        >>> b.remove(2)
        >>> b
        Bag([])
        >>> b.remove(3)
        Traceback (most recent call last):
        ValueError: 3 not in Bag
        """
        try:
            self._data.remove(value)
        except ValueError:
            raise ValueError(
                f"{value} not in {self.__class__.__name__}"
            ) from None

    def count(self, value: Any) -> int:
        """Count the number of times value appears in the Bag.

        >>> b = Bag([1, 2, 2])
        >>> b.count(1)
        1
        >>> b.count(2)
        2
        """
        return self._data.count(value)

    def randpop(self) -> Any:
        """Pop a random object from the Bag.

        >>> b = Bag([1, 2, 3])
        >>> b.randpop() in {1, 2, 3}
        True
        """
        value: Any = _choice(self._data)
        self._data.remove(value)
        return value

    def as_counter(self) -> Counter:
        """Return a Counter from the object in the Bag.

        >>> b = Bag([1, 2, 2])
        >>> b.as_counter()
        Counter({2: 2, 1: 1})
        >>> b = Bag([[1, 2], 3, 4])
        >>> b.as_counter()
        Traceback (most recent call last):
        TypeError: unhashable type: 'list'
        """
        try:
            return Counter(self._data)
        except TypeError:
            raise

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, value: Any) -> bool:
        return value in self._data

    def __iter__(self):
        yield from self._data

    def __reversed__(self):
        yield from reversed(self._data)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._data})"

    def __str__(self) -> str:
        return self.__repr__()
