# Abstract Data Types in Python

![Python Build](https://github.com/lpozo/pydata-structures/actions/workflows/python-package.yml/badge.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

Basic Python implementation for several Abstract data types. Just a learning exercise.

## Table of Content

- [Array](#array)
- [Bag (multisets)](#bag-multisets)
- [Matrix](#matrix)
- [Queue](#queue)
- [Stack](#stack)
- [Singly Linked List](#singly-linked-list)

## Array

A one-dimensional array is a sequence of items stored in contiguous memory locations. They allow random access to the individual items. They must contain data of the same type and have a fixed size that can't vary during the array lifetime.

This implementation uses a `ctypes.py_object` to store and manage the data. It defines the following operations:

| Operation              | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `array = Array(size)`  | Build an array that can hold `size` items.                   |
| `array[index]`         | Retrieve the item at `index`.                                |
| `array[index] = value` | Assign `value` to the item at `index`.                       |
| `array.clear()`        | Remove all the items form the `array`.                       |
| `len(array)`           | Return the length of the `array`.                            |
| `item in array`        | Return `True` if `item` exists in `array`, `False` otherwise. |

It also supports iteration and reverse iteration.

## Bag (multisets)

A bag, also known as [multiset](https://en.wikipedia.org/wiki/Multiset), is a container like a shopping bag. It's a set-like container that allows multiple instances of a given value. You can use a bag to store a collection of items. Bags restrict access to individual items.

This implementation uses a [`list`](https://docs.python.org/3/library/stdtypes.html#list) to store and manage the data. It defines the following operations:

| Operation             | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| `bag = Bag()`         | Build an empty `bag`.                                       |
| `bag = Bag(iterable)` | Build a `bag` with items from iterable.                     |
| `bag.add(item)`       | Add `item` the to `bag`.                                    |
| `bag.remove(item)`    | Remove `item` from `bag`.                                   |
| `bag.pop()`           | Pop an item from the right end of `bag`.                    |
| `bag.clear()`         | Remove all the items from `bag`.                            |
| `len(bag)`            | Return the length of the `bag`.                             |
| `item in bag`         | Return `True` if `item` exists in `bag`, `False` otherwise. |
| `bag.count(item)`     | Count the frequency of `item` in the `bag`.                  |

It also supports iteration and reverse iteration.

## Matrix

A [matrix](https://en.wikipedia.org/wiki/Matrix_(mathematics)) is a collection of numbers arranged in rows and columns as a rectangular grid of a fixed size. Matrices are quite useful in several areas, such as [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) and [computer graphics](https://en.wikipedia.org/wiki/Computer_graphics). You can use matrices for representing and solving systems of [linear equations](https://en.wikipedia.org/wiki/Linear_equation), for example.

This implementation uses a [`list`](https://docs.python.org/3/library/stdtypes.html#list) to store and manage the data. It defines the following operations:

| Operation                              | Description                                                  |
| -------------------------------------- | ------------------------------------------------------------ |
| `matrix = Matrix(rows, cols)`          | Build a `matrix` of size `rows` x `cols`.                    |
| `matrix = Matrix(rows, cols, default)` | Build a `matrix` of size `rows` x `cols`, which values default to `default`. |
| `matrix.rows`                          | Return the number of rows in `matrix`.                       |
| `matrix.cols`                          | Return the number of columns in `matrix`.                    |
| `matrix.size`                          | Return the size of `matrix` as a tuple of `cols` and `rows`. |
| `matrix.scale_by(scalar)`              | Scale the whole `matrix` by `scalar`.                        |
| `matrix.transpose()`                   | Return a new matrix, which is the transpose of `matrix`.     |
| `matrix.add(other)`                    | Return a new matrix, which is the addition of `matrix` and `other`. |
| `matrix + other`                       | Return a new matrix, which is the addition of `matrix` and `other`. |
| `matrix.subtract(other)`               | Return a new matrix, which is the subtraction of `matrix` and `other`. |
| `matrix - other`                       | Return a new matrix, which is the subtraction of `matrix` and `other`. |
| `matrix.multiply(other)`                | Return a new matrix, which is the multiplication of `matrix` and `other`. |
| `matrix * other`                       | Return a new matrix, which is the multiplication of `matrix` and `other`. |
| `matrix[i, j]`                         | Retrieve the value at cell `(i, j)` from `matrix`.           |
| `matrix[i, j] = value`                 | Assign `value` to the cell `(i, j)` of `matrix`.             |
| `Matrix.from_list_of_lists(iterable)`  | Build a new matrix from a list of lists. It's a class method. |

It doesn't support direct iteration.

## Queue

A queue is a [collection](https://en.wikipedia.org/wiki/Collection_(abstract_data_type)) of items. You can modify queues by adding items at one end and removing items from the opposite end.

Queues manage their items in a **first in**, **first out** ([FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))) fashion. They work as a pipe where you push in new items at one end of the pipe and pop old items out from the other end. Adding an item to one end of a queue is known as an **enqueue** operation. Removing an item from the other end is called **dequeue**.

This implementation uses a [`collections.deque`](https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque) to store and manage the data. It defines the following operations:

| Operation                 | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `queue = Queue()`         | Build an empty `queue`.                                      |
| `queue = Queue(iterable)` | Build a `queue` with items from `iterable`.                  |
| `queue.enqueue(item)`     | Add `item` to the right end of the `queue`.                  |
| `queue.dequeue()`         | Pop the item at the left end of the `queue`.                 |
| `queue.remove(item)`      | Remove `item` from the `queue`.                              |
| `queue.is_empty()`        | Return `True` if the `queue` is empty, `False` otherwise.    |
| `queue.front()`           | Return the item at the left end of the `queue` without popping it. |
| `len(queue)`              | Return the length of the `queue`.                            |
| `item in queue`           | Return `True` if `item` exists in `queue`, `False` otherwise. |

It also supports iteration and reverse iteration.

## Stack

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a data structure where access is only at one end of the sequence. New values are pushed onto the stack to add them to the sequence and popped off the stack to remove them from the sequence. Stacks are used in many algorithms in computer science. They're useful when parsing information. Stacks are called **last in**, **first out** ([LIFO](https://en.wikipedia.org/wiki/FIFO_and_LIFO_accounting#LIFO)) data structures. The last item pushed is the first item popped.

This implementation uses a [`collections.deque`](https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque) to store and manage the data. It defines the following operations:

| Operation                 | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `stack = Stack()`         | Build an empty `stack`.                                      |
| `stack = Stack(iterable)` | Build a `stack` with items from `iterable`.                  |
| `stack.push(item)`        | Push `item` onto the top of the `stack`.                     |
| `stack.pop()`             | Pop the item at the top of the `stack`.                      |
| `stack.top()`             | Return the item at the top of the `stack` without popping it. |
| `stack.is_empty()`        | Return `True` if the `stack` is empty, `False` otherwise.    |
| `len(stack)`              | Return the length of the `stack`.                            |
| `item in stack`           | Return `True` if `item` exists in `stack`, `False` otherwise. |

It also supports iteration and reverse iteration.

## Singly Liked List

A [linked list](https://en.wikipedia.org/wiki/Linked_list) is a linear collection of data where each item in the list is stored in a separate [node](https://en.wikipedia.org/wiki/Node_(computer_science)). A node stores two pieces of information: a data item and a reference to the next node in the linked list, often called `.next`.

The order of nodes doesn't follow a sequence of contiguous physical memory locations. Nodes are linked in a chain, in which each node holds a reference to the next one.

This implementation defines the following operations:

| Operation                    | Description                                             |
| ---------------------------- | ------------------------------------------------------- |
| `llist.append_left(value)`   | Add a node holding `value` to the left end of `llist`.  |
| `llist.append(value)`        | Add a node holding `value` to the right end of `llist`. |
| `llist.insert(index, value)` | Insert a node holding `value` at `index`.               |
| `llist.remove(value)`        | Remove the node holding `value` from `llist`.           |
| `llist.reverse()`            | Reverse the `llist` in place.                           |

It also supports iteration.

## Authors

- Leodanis Pozo Ramos -> GitHub: [@lpozo](https://www.github.com/lpozo) -> Twitter: [@lpozo78](https://twitter.com/lpozo78) -> Web: <https://leodanispozo.netlify.app>

## License

[MIT](https://choosealicense.com/licenses/mit/)
