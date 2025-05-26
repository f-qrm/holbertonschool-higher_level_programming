#!/usr/bin/python3
"""
This module provides a function to check if an object is a subclass instance.

It contains a function `inherits_from` that determines whether an object
is an instance of a subclass of a given class, but not an instance of the
class itself.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a subclass of a specified class.

    This function returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class,
    but not if the object is an instance of the class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
        (but not a_class itself),
              otherwise False.
    """
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    return False
