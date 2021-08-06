"""Map abstract data type."""

from typing import Any, Iterator, List, Mapping, Optional, Tuple


class Map:
    """Map abstract data type based on lists.

    >>> m = Map({"one": 1, "two": 2})
    >>> m
    Map({'one': 1, 'two': 2})

    >>> m = Map(one=1, two=2)
    >>> m
    Map({'one': 1, 'two': 2})

    >>> m = Map({"one": 1}, two=2)
    >>> m
    Map({'one': 1, 'two': 2})
    >>> print(m)
    {'one': 1, 'two': 2}

    >>> m["one"]
    1
    >>> m["two"]
    2
    >>> m["three"]
    Traceback (most recent call last):
    KeyError: 'three'
    >>> m["three"] = 3
    >>> m
    Map({'one': 1, 'two': 2, 'three': 3})
    >>> for key in m:
    ...     print(key)
    one
    two
    three
    >>> len(m)
    3
    >>> m.get("one")
    1
    >>> del m["three"]
    >>> m
    Map({'one': 1, 'two': 2})
    """

    def __init__(
        self, mapping: Optional[Mapping[Any, Any]] = None, /, **kwargs
    ) -> None:
        self._keys: List[Any] = []
        self._values: List[Any] = []
        if mapping is not None:
            for key, value in mapping.items():
                self[key] = value
        if kwargs:
            for key, value in kwargs.items():
                self[key] = value

    def keys(self) -> Iterator[Any]:
        """Return an iterator over the keys of map.

        >>> m = Map(one=1, two=2)
        >>> for key in m.keys():
        ...     print(key)
        one
        two
        """
        yield from self._keys

    __iter__ = keys

    def values(self) -> Iterator[Any]:
        """Return an iterator over the values of map.

        >>> m = Map(one=1, two=2)
        >>> for value in m.values():
        ...     print(value)
        1
        2
        """
        yield from self._values

    def items(self) -> Iterator[Tuple[Any, Any]]:
        """Return an iterator that yields key-value tuples.

        >>> m = Map(one=1, two=2)
        >>> for key, value in m.items():
        ...     print(key, "->", value)
        one -> 1
        two -> 2
        """
        yield from zip(self._keys, self._values)

    def update(
        self, other: Optional[Mapping[Any, Any]] = None, /, **kwargs
    ) -> None:
        """Update map with items from other.

        >>> m = Map(one=1, two=2)
        >>> m
        Map({'one': 1, 'two': 2})
        >>> m.update({"two": 22, "three": 3})
        >>> m
        Map({'one': 1, 'two': 22, 'three': 3})
        """
        if other is not None:
            for key, value in other.items():
                self[key] = value
        if kwargs:
            for key, value in kwargs.items():
                self[key] = value

    def clear(self) -> None:
        """Remove all the items from map.

        >>> m = Map(one=1, two=2)
        >>> m
        Map({'one': 1, 'two': 2})
        >>> m.clear()
        >>> m
        Map({})
        """
        self._keys.clear()
        self._values.clear()

    def __getitem__(self, key: Any) -> Any:
        try:
            index = self._keys.index(key)
        except ValueError:
            raise KeyError(f"{key}") from None
        return self._values[index]

    get = __getitem__

    def __setitem__(self, key: Any, value: Any) -> None:
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def set_default(self, key, default: Optional[Any] = None, /) -> Any:
        """Insert a key-default pair into map if key doesn't exist.

        Return the value for key if key is in the dictionary, else default.

        >>> m = Map()
        >>> m.set_default("one", 1)
        1
        >>> m.set_default("two")
        >>> m["two"] is None
        True
        """
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default

    def __len__(self) -> int:
        return len(self._keys)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({dict(zip(self._keys, self._values))})"
        )

    def __str__(self) -> str:
        return f"{dict(zip(self._keys, self._values))}"

    def __delitem__(self, key):
        try:
            index = self._keys.index(key)
        except ValueError:
            raise KeyError(f"{key}") from None
        del self._keys[index]
        del self._values[index]
