
# Abstract Data Types in Python

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

Basic Python implementation for several Abstract data types. Just a learning exercise.

**Table of Content**

  - [Array](#array)
  - [Bag (multisets)](#bag-multisets)
  - [Queue](#queue)
  - [Stack](#stack)

## Array

A one-dimensional array is a sequence of items stored in contiguous memory locations. They allow random access to the individual items. They must contain data of the same type and have a fixed size that can't vary during the array lifetime.

This implementation uses a `ctypes.py_object` to store and manage the data. It defines the following operations:

| Operation              | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `array[index]`         | Retrieve the item at `index`.                                |
| `array[index] = value` | Assign `value` to the item at `index`.                       |
| `array.clear()`        | Remove all the items form the `array`.                       |
| `len(array)`           | Return the length of the `array`.                            |
| `item in array`        | Return `True` if `item` exists in `array`, `False` otherwise. |

It also supports iteration and reverse iteration.

## Bag (multisets)

A bag, also known as [multiset](https://en.wikipedia.org/wiki/Multiset), is a container like a shopping bag. It's a set-like container that allows multiple instances of a given value. You can use a bag to store a collection of items. Bags restrict access to individual items.

This implementation uses a [`list`](https://docs.python.org/3/library/stdtypes.html#list) to store and manage the data. It defines the following operations:

| Operation          | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| `bag.add(item)`    | Add `item` the to `bag`.                                    |
| `bag.remove(item)` | Remove `item` from `bag`.                                   |
| `bag.pop()`        | Pop an item from the right end of `bag`.                    |
| `bag.clear()`      | Remove all the items from `bag`.                            |
| `len(bag)`         | Return the length of the `bag`.                             |
| `item in bag`      | Return `True` if `item` exists in `bag`, `False` otherwise. |
| `bag.count(item)`  | Conut the frequncy of `item` in the `bag`.                  |

It also supports iteration and reverse iteration.

## Queue

A queue is a [collection](https://en.wikipedia.org/wiki/Collection_(abstract_data_type)) of items. You can modify queues by adding items at one end and removing items from the opposite end.

Queues manage their items in a **first in**, **first out** ([FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))) fashion. They work as a pipe where you push in new items at one end of the pipe and pop old items out from the other end. Adding an item to one end of a queue is known as an **enqueue** operation. Removing an item from the other end is called **dequeue**.

This implementation uses a [`collections.deque`](https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque) to store and manage the data. It defines the following operations:

| Operation             | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `queue.enqueue(item)` | Add `item` to the right end of the `queue`.                  |
| `queue.dequeue()`     | Pop the item at the left end of the `queue`.                 |
| `queue.remove(item)`  | Remove `item` from the `queue`.                              |
| `queue.is_empty()`    | Return `True` if the `queue` is empty, `False` otherwise.    |
| `queue.front()`       | Return the item at the left end of the `queue` without popping it. |
| `len(queue)`          | Return the length of the `queue`.                            |
| `item in queue`       | Return `True` if `item` exists in `queue`, `False` otherwise. |

It also supports iteration and reverse iteration.

## Stack

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a data structure where access is only at one end of the sequence. New values are pushed onto the stack to add them to the sequence and
popped off the stack to remove them from the sequence. Stacks are used in many algorithms in computer science. They're useful when parsing information. Stacks are called **last in**, **first out** ([LIFO](https://en.wikipedia.org/wiki/FIFO_and_LIFO_accounting#LIFO)) data structures. The last item pushed is the first item popped.

This implementation uses a [`collections.deque`](https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque) to store and manage the data. It defines the following operations:

| Operation          | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| `stack.push(item)` | Push `item` onto the top of the `stack`.                     |
| `stack.pop()`      | Pop the item at the top of the `stack`.                      |
| `stack.top()`      | Return the item at the top of the `stack` without popping it. |
| `stack.is_empty()` | Return `True` if the `stack` is empty, `False` otherwise.    |
| `len(stack)`       | Return the length of the `stack`.                            |
| `item in stack`    | Return `True` if `item` exists in `stack`, `False` otherwise. |

It also supports iteration and reverse iteration.

## Authors

- Leodanis Pozo Ramos - [@lpozo](https://www.github.com/lpozo)

## License

[MIT](https://choosealicense.com/licenses/mit/)
