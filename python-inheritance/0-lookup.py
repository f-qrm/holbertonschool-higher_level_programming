#!/usr/bin/python3
"""
This module provides a single function that retrieves
a list of available attributes and methods of an object.

It can be used for introspection to explore the capabilities
of a given Python object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of the given object.

    This function uses the built-in dir() function to return all
    the attributes and methods that are accessible via the object.
    It is useful for understanding the behavior and capabilities
    of any Python object, including user-defined classes and built-in types.
    """
    return dir(obj)
