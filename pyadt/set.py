"""Set abstract data type."""

from typing import Any, Iterator, List, Optional, Sequence


class Set:
    """Implement a Set abstract data type.

    >>> s = Set()
    >>> s
    Set([])

    >>> s = Set([])
    >>> s
    Set([])

    >>> s = Set([1, 2, 3])
    >>> s
    Set([1, 2, 3])

    >>> s = Set([1, 2, 3, 3, 3])
    >>> s
    Set([1, 2, 3])
    >>> len(s)
    3
    """

    def __init__(self, iterable: Optional[Sequence[Any]] = None, /) -> None:
        self._data: List[Any] = []
        if iterable is not None and len(iterable) > 0:
            for element in iterable:
                self.__add(element)

    def add(self, element: Any) -> None:
        """Add element to set.

        >>> s = Set([])
        >>> s.add(1)
        >>> s
        Set([1])
        >>> s.add(2)
        >>> s
        Set([1, 2])
        >>> s.add([3, 4])
        Traceback (most recent call last):
        TypeError: unhashable type: 'list'
        """
        hash(element)
        if element not in self._data:
            self._data.append(element)

    __add = add  # Avoid breaking the class by a subclasser

    def remove(self, element: Any) -> None:
        """Remove an element from set.

        >>> s = Set([1, 2])
        >>> s.remove(2)
        >>> s
        Set([1])
        >>> s.remove(42)
        Traceback (most recent call last):
        KeyError: '42 not in set'
        """
        try:
            self._data.remove(element)
        except ValueError:
            raise KeyError(f"{element} not in set") from None

    def discard(self, element: Any) -> None:
        """Remove element from set if present.

        >>> s = Set([1, 2])
        >>> s.discard(1)
        >>> s
        Set([2])
        >>> s.discard(100)
        >>> s
        Set([2])
        """
        try:
            self._data.remove(element)
        except ValueError:
            pass

    def pop(self) -> Any:
        """Pop an element from set.

        >>> s = Set([1, 2])
        >>> s.pop()
        2
        >>> s.pop()
        1
        >>> s.pop()
        Traceback (most recent call last):
        KeyError: 'pop from an empty set'
        """
        try:
            return self._data.pop()
        except IndexError:
            raise KeyError("pop from an empty set") from None

    def clear(self) -> None:
        """Remove all the elements from set.

        >>> s = Set([1, 2, 3])
        >>> s.clear()
        >>> s
        Set([])
        >>> s.clear()
        """
        self._data.clear()

    def update(self, other: "Set") -> None:
        """Update set with elements from other.

        >>> s = Set([1, 2, 3])
        >>> o = Set([4, 5, 6])
        >>> s.update(o)
        >>> s
        Set([1, 2, 3, 4, 5, 6])
        >>> s.update([7, 8, 9])
        Traceback (most recent call last):
        TypeError: Set object expected
        """
        self._validate_other(other)
        for element in other:
            self.__add(element)

    def _validate_other(self, other) -> None:
        if other.__class__ is not self.__class__:
            raise TypeError("Set object expected")

    def is_subset(self, other: "Set") -> bool:
        """Return True if set is subset of other, False otherwise.

        >>> s = Set([1, 2, 3])
        >>> o = Set([1, 2, 3, 4, 5])
        >>> s.is_subset(o)
        True
        >>> a = Set([2, 4, 6])
        >>> a.is_subset(o)
        False
        """
        self._validate_other(other)
        for element in self:
            if element not in other:
                return False
        return True

    def is_superset(self, other: "Set") -> bool:
        """Return True if set is superset of other, False otherwise.

        >>> s = Set([1, 2, 3])
        >>> o = Set([1, 2, 3, 4, 5])
        >>> o.is_superset(s)
        True
        >>> s.is_superset(o)
        False
        """
        self._validate_other(other)
        for element in other:
            if element not in self:
                return False
        return True

    def is_disjoint(self, other: "Set") -> bool:
        """Return True if set has no elements in common with other.

        >>> s = Set([1, 2, 3])
        >>> o = Set([4, 5, 6])
        >>> s.is_disjoint(o)
        True
        >>> a = Set([2, 4, 6])
        >>> s.is_disjoint(a)
        False
        """
        self._validate_other(other)
        for element in self:
            if element in other:
                return False
        return True

    def union(self, other: "Set") -> "Set":
        """Return a new set that is the union of set and other.

        >>> s = Set([1, 2, 3])
        >>> o = Set([1, 4, 5])
        >>> s.union(o)
        Set([1, 2, 3, 4, 5])
        """
        self._validate_other(other)
        new_set = type(self)()
        new_set._data.extend(self._data)
        for element in other:
            new_set.__add(element)
        return new_set

    def intersection(self, other: "Set") -> "Set":
        """Return a new set that is the intersection of set with other.

        >>> s = Set([1, 2, 3])
        >>> o = Set([2, 4, 3, 6])
        >>> s.intersection(o)
        Set([2, 3])
        >>> o.intersection(s)
        Set([2, 3])
        """
        self._validate_other(other)
        new_set = type(self)()
        for element in self:
            if element in other:
                new_set.__add(element)
        return new_set

    def difference(self, other: "Set") -> "Set":
        """Return a new set with the difference between set and other.

        >>> s = Set([1, 2, 3])
        >>> o = Set([2, 4, 3, 6])
        >>> s.difference(o)
        Set([1])
        >>> o.difference(s)
        Set([4, 6])
        """
        self._validate_other(other)
        new_set = type(self)()
        for element in self:
            if element not in other:
                new_set.__add(element)
        return new_set

    def __eq__(self, other: "Set") -> bool:
        self._validate_other(other)
        return sorted(self._data) == sorted(other._data)

    def __len__(self) -> int:
        return len(self._data)

    def __contain__(self, element: Any) -> bool:
        return element in self._data

    def __iter__(self) -> Iterator:
        yield from self._data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._data})"

    __str__ = __repr__
