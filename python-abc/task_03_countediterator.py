#!/usr/bin/env python3
"""
This module defines a custom iterator class called `CountedIterator`.

`CountedIterator` wraps around any iterable and counts how many elements
have been accessed through iteration.
"""


class CountedIterator:
    """
    CountedIterator is a custom iterator that wraps around another iterable
    and counts the number of elements retrieved using `next()`.

    It can be useful for monitoring iteration progress or for debugging
    purposes.
    """
    def __init__(self, count):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            count (iterable): Any iterable object (e.g. list, tuple,
            generator).
        """
        self.iterat = iter(count)
        self.j = 0

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: The current iterator instance.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterable and increment the count.

        Returns:
            any: The next item in the iterable.

        Raises:
            StopIteration: When the iterable is exhausted.
        """
        item = next(self.iterat)
        self.j += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been retrieved from the iterator.

        Returns:
            int: The count of accessed items.
        """
        return self.j
