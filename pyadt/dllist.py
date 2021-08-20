"""Doubly Linked List abstract data type."""


from typing import Any, Sequence, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.previous: Optional[Node] = None
        self.next: Optional[Node] = None


class DoublyLinkedList:
    def __init__(self, iterable: Optional[Sequence[Any]] = None, /) -> None:
        self.head: Optional[Node] = None
        self._length = 0
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

    def append_left(self, value: Any) -> None:
        """Add a node holding value to the left end of the doubly linked list.

        >>> dll = LinkedList([2, 3])
        >>> dll.append_left(1)
        >>> dll
        DoublyLinkedList([1, 2, 3])
        """
        node = Node(data=value)
        node.next = self.head
        self.head = node
        self._length += 1
