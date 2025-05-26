#!/usr/bin/python3
"""
This module defines a class that inherits from the built-in list class
and adds a method to print the list in sorted (ascending) order
without modifying the original list.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class.

    It provides an additional method called print_sorted that prints
    the list elements in ascending order, without altering the list itself.
    """
    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.

        The original list remains unchanged. This method simply uses
        the built-in `sorted()` function to sort and print the elements.
        """
        print(sorted(self))
