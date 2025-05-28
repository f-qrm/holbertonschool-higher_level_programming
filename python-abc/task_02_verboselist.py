#!/usr/bin/env python3
"""
This module defines a custom list subclass called `VerboseList`.

The `VerboseList` class behaves like a normal Python list,
but it provides additional console output for certain list operations,
helping users understand what is happening during list modifications.
"""


class VerboseList(list):
    """
    VerboseList is a subclass of the built-in list class.

    It overrides some common list methods to print messages
    whenever items are added, removed, or modified in the list.
    This can be useful for debugging or learning purposes.
    """

    def append(self, item):
        """
        Append an item to the end of the list and print a message.

        Args:
            item (any): The item to append to the list.

        Example:
            >>> v = VerboseList()
            >>> v.append(10)
            Added [10] to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """
        Extend the list by appending elements from the iterable
        and print a message.

        Args:
            x (iterable): An iterable (e.g. list or tuple) whose
            items will be added.

        Example:
            >>> v = VerboseList([1])
            >>> v.extend([2, 3])
            Extended the list with [2] items.
        """
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list
        and print a message.

        Args:
            item (any): The item to remove from the list.

        Example:
            >>> v = VerboseList([1, 2, 3])
            >>> v.remove(2)
            Removed [2] from the list.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, i=-1):
        """
        Remove and return the item at the given position, and
        print a message.

        Args:
            i (int, optional): The index of the item to remove.
            Defaults to -1 (last item).

        Returns:
            any: The item that was removed.

        Example:
            >>> v = VerboseList([1, 2, 3])
            >>> v.pop()
            Popped [3] from the list.
        """
        item = super().pop(i)
        print(f"Popped {[item]} from the list.")
        return item
