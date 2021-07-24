class Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None


class BinaryTree:
    def __init__(self, root) -> None:
        self._root = root
