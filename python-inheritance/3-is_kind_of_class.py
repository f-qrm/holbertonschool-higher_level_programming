#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a given class or an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or its subclass.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or any subclass of it,
              False otherwise.
    """
    return isinstance(obj, a_class)
