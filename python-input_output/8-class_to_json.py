#!/usr/bin/python3
"""
This module provides a function that returns the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj (any): An instance of a class with serializable attributes.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
