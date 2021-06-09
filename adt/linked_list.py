"""Linked list abstract data type."""


class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
        else:
            for current_node in self:
                pass
            current_node.next = node

    def insert(self, possition, node):
        if self.head is None or possition == 0:
            self.add_first(node)
            return
        previous_node = self.head
        for i, current_node in enumerate(self):
            if i == possition:
                previous_node.next = node
                node.next = current_node
                return
            previous_node = current_node
        raise IndexError("index out of range")

    def remove(self, position):
        if self.head is None:
            return
        previous_node = self.head
        for i, current_node in enumerate(self):
            if i == position:
                previous_node.next = current_node.next
                return
            previous_node = current_node
        raise IndexError("index out of range")

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        if len(nodes) == 1:
            return f"HEAD({nodes[0]})"
        return f"HEAD({nodes[0]}) -> " + " -> ".join(nodes[1:])

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return f"{self.__class__.__name__}({nodes})"

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def reverse(self):
        previous = None
        current = self.head
        next_node = current.next
        while current:
            current.next = previous
            previous = current
            current = next_node
            if next_node:
                next_node = next_node.next
        self.head = previous


class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

    def __repr__(self) -> str:
        return self.data
