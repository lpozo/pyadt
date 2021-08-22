"""Doubly Linked List abstract data type."""


from typing import Any, Iterator, Sequence, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.previous: Optional[Node] = None
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(data={self.data})"


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
        >>> dll = DoublyLinkedList()
        >>> dll.append(0)
        >>> dll
        DoublyLinkedList([0])
        """
        node = Node(data=value)
        if self.tail is not None:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.append_left(value)
        self._length += 1

    def __repr__(self) -> str:
        data = [node.data for node in self]
        return f"{self.__class__.__name__}({data})"

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
