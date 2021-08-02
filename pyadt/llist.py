"""Linked list abstract data type."""


from typing import Any, Iterator, List, Optional


class Node:
    """Node of a linked list."""

    def __init__(self, data: Any) -> None:
        self.next: Optional["Node"] = None
        self.data = data

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    """Linked list abstract data type."""

    def __init__(self, data: Optional[List[Any]] = None) -> None:
        """Initialize the LinkedList with data.

        >>> ll = LinkedList([1, 2, 3])
        >>> ll
        LinkedList([1, 2, 3])
        >>> ll.head
        1
        >>> print(ll)
        HEAD(1) -> 2 -> 3 -> None

        >>> ll = LinkedList()
        >>> ll
        LinkedList([])

        >>> ll = LinkedList([])
        >>> print(ll)
        HEAD(None)
        """
        self.head: Optional[Node] = None
        self._length: int = 0

        if data is not None and (length := len(data)) > 0:
            head, *rest = data
            self._length = length
            self.head = Node(data=head)
            node = self.head
            for value in rest:
                node.next = Node(data=value)
                node = node.next

    def append_left(self, value: Any) -> None:
        """Add a node holding value to the left end of the linked list.

        >>> ll = LinkedList([2, 3])
        >>> ll.append_left(1)
        >>> ll
        LinkedList([1, 2, 3])
        """
        node = Node(data=value)
        node.next = self.head
        self.head = node
        self._length += 1

    def append(self, value: Any) -> None:
        """Add a node holding value to the right end of the linked list.

        >>> ll = LinkedList([1, 2])
        >>> ll.append(3)
        >>> ll
        LinkedList([1, 2, 3])
        """
        node = Node(data=value)

        if self.head is None:
            self.head = node
        else:
            # Traverse the list to reach the last node, no other action done
            for last_node in self:
                pass
            last_node.next = node

        self._length += 1

    def insert(self, index: int, value: Any) -> None:
        """Insert a node holding value at index.

        >>> ll = LinkedList()
        >>> ll.insert(0, 1)
        >>> ll
        LinkedList([1])

        >>> ll = LinkedList([1, 3])
        >>> ll.insert(1, 2)
        >>> ll
        LinkedList([1, 2, 3])
        >>> ll = LinkedList([1, 2])
        >>> ll.insert(2, 3)
        Traceback (most recent call last):
        IndexError: index out of range
        """
        node = Node(data=value)

        if self.head is None or index == 0:
            self.append_left(node)
            return

        previous_node = self.head
        for i, current_node in enumerate(self):
            if i == index:
                previous_node.next = node
                node.next = current_node
                self._length += 1
                return
            previous_node = current_node

        raise IndexError("index out of range")

    def remove(self, value: Any) -> None:
        """Remove the node holding value.

        >>> ll = LinkedList()
        >>> ll.remove(1)
        >>> ll
        LinkedList([])

        >>> ll = LinkedList([1, 2, 3])
        >>> ll.remove(1)
        >>> ll
        LinkedList([2, 3])

        >>> ll = LinkedList([1, 2, 3])
        >>> ll.remove(2)
        >>> ll
        LinkedList([1, 3])

        >>> ll = LinkedList([1, 2, 3])
        >>> ll.remove(3)
        >>> ll
        LinkedList([1, 2])

        >>> ll.remove(4)
        Traceback (most recent call last):
        IndexError: 4 doesn't exist
        """
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        previous_node = self.head
        for current_node in self:
            if current_node.data == value:
                previous_node.next = current_node.next
                self._length -= 1
                return
            previous_node = current_node

        raise IndexError(f"{value} doesn't exist")

    def reverse(self) -> None:
        """Reverse the list in place.

        >>> ll = LinkedList([1, 2, 3])
        >>> ll.reverse()
        >>> ll
        LinkedList([3, 2, 1])

        >>> ll = LinkedList()
        >>> ll.reverse()
        >>> ll
        LinkedList([])
        """
        if self.head is None:
            return

        previous: Optional[Node] = None
        current: Optional[Node] = self.head
        next: Optional[Node] = current.next
        while current:
            current.next = previous
            previous = current
            current = next
            if next:
                next = next.next
        self.head = previous

    def __iter__(self) -> Iterator:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = self._nodes_as_list()
        return f"{self.__class__.__name__}({nodes})"

    def _nodes_as_list(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return nodes

    def __str__(self) -> str:
        nodes = [str(data) for data in self._nodes_as_list()]
        nodes.append("None")
        if len(nodes) == 1:
            return f"HEAD({nodes[0]})"
        return f"HEAD({nodes[0]}) -> " + " -> ".join(nodes[1:])

    def __len__(self):
        return self._length
