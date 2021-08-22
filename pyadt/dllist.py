"""Doubly Linked List abstract data type."""


from typing import Any, Iterator, Optional, Sequence


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.previous: Optional[Node] = None
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(data={self.data})"

    def __eq__(self, other: "Node") -> bool:
        if other.__class__ is not self.__class__:
            raise TypeError("Node object expected")
        return self.data == other.data


class DoublyLinkedList:
    """Doubly Linked List abstract data type.

    >>> dll = DoublyLinkedList([1, 2, 3])
    >>> dll
    DoublyLinkedList([1, 2, 3])
    >>> dll.head.data
    1
    >>> dll.tail.data
    3
    >>> dll.head
    Node(data=1)
    >>> dll.tail
    Node(data=3)
    >>> for node in dll:
    ...     print(node)
    Node(data=1)
    Node(data=2)
    Node(data=3)
    >>> for node in reversed(dll):
    ...     print(node)
    Node(data=3)
    Node(data=2)
    Node(data=1)
    >>> len(dll)
    3
    >>> print(dll)
    HEAD(1) <-> 2 <-> 3 <-> None
    """

    def __init__(self, iterable: Optional[Sequence[Any]] = None, /) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._length: int = 0
        if iterable is not None and (length := len(iterable)) > 0:
            head, *rest = iterable
            self._length = length
            self.head = Node(data=head)
            current = self.head
            for value in rest:
                current.next = Node(data=value)
                previous = current
                current = current.next
                current.previous = previous
            self.tail = current

    def append_left(self, value: Any) -> None:
        """Add a node holding value to the left end of the doubly linked list.

        >>> dll = DoublyLinkedList([1, 2, 3])
        >>> dll.append_left(0)
        >>> dll
        DoublyLinkedList([0, 1, 2, 3])
        >>> len(dll)
        4
        >>> dll = DoublyLinkedList()
        >>> dll.append_left(0)
        >>> dll
        DoublyLinkedList([0])
        """
        node = Node(data=value)
        if self.head is not None:
            node.next = self.head
            self.head.previous = node
        self.head = node
        self._length += 1

    __append_left = append_left

    def append(self, value: Any) -> None:
        """Add a node holding value to the right end of the linked list.

        >>> dll = DoublyLinkedList([0, 1, 2])
        >>> len(dll)
        3
        >>> dll.append(3)
        >>> dll
        DoublyLinkedList([0, 1, 2, 3])
        >>> len(dll)
        4
        >>> dll.head
        Node(data=0)
        >>> dll.tail
        Node(data=3)
        >>> dll = DoublyLinkedList()
        >>> dll.append(0)
        >>> dll
        DoublyLinkedList([0])
        >>> dll.tail == dll.head
        True
        """
        node = Node(data=value)
        if self.tail is not None:
            node.previous = self.tail
            self.tail.next = node
        else:
            self.__append_left(value)
        self.tail = node
        self._length += 1

    def remove(self, value: Any) -> None:
        """Remove the node holding value.

        >>> dll = DoublyLinkedList()
        >>> dll.remove(1)
        >>> dll
        DoublyLinkedList([])
        >>> dll = DoublyLinkedList([1, 2, 3])
        >>> dll.remove(1)
        >>> dll
        DoublyLinkedList([2, 3])
        >>> dll = DoublyLinkedList([1, 2, 3])
        >>> dll.remove(2)
        >>> dll
        DoublyLinkedList([1, 3])
        >>> dll = DoublyLinkedList([1, 2, 3])
        >>> dll.remove(3)
        >>> dll
        DoublyLinkedList([1, 2])
        >>> dll.remove(4)
        Traceback (most recent call last):
        IndexError: 4 doesn't exist
        """
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            self.head.previous = None
            self._length -= 1
            return

        if self.tail.data == value:
            self.tail = self.tail.previous
            self.tail.next = None
            self._length -= 1
            return

        previous = self.head
        for node in self:
            if node.data == value:
                next = node.next
                previous.next = next
                next.previous = previous
                self._length -= 1
                return
            previous = node

        raise IndexError(f"{value} doesn't exist")

    def insert(self, index: int, value: Any) -> None:
        """Insert a node holding value at index.

        >>> dll = DoublyLinkedList()
        >>> dll.insert(0, 1)
        >>> dll
        DoublyLinkedList([1])
        >>> len(dll)
        1
        >>> dll = DoublyLinkedList([1, 3])
        >>> dll.insert(1, 2)
        >>> dll
        DoublyLinkedList([1, 2, 3])
        >>> len(dll)
        3
        >>> dll = DoublyLinkedList([1, 2])
        >>> dll.insert(2, 3)
        Traceback (most recent call last):
        IndexError: index out of range
        """
        if self.head is None or index == 0:
            self.__append_left(value)
            return

        previous = self.head
        for i, current in enumerate(self):
            if i == index:
                node = Node(data=value)
                previous.next = node
                node.next = current
                node.previous = previous
                self._length += 1
                return
            previous = current

        raise IndexError("index out of range")

    def __repr__(self) -> str:
        data = [node.data for node in self]
        return f"{self.__class__.__name__}({data})"

    def __str__(self) -> str:
        data = [str(node.data) for node in self]
        data.append("None")
        if len(data) == 1:
            return f"HEAD({data[0]})"
        return f"HEAD({data[0]}) <-> " + " <-> ".join(data[1:])

    def __iter__(self) -> Iterator:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __reversed__(self) -> Iterator:
        node = self.tail
        while node is not None:
            yield node
            node = node.previous

    def __len__(self):
        return self._length
