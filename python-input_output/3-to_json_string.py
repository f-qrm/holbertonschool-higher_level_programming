#!/usr/bin/python3
"""
3-to_json_string.py

This module provides a function that returns the JSON representation of an
object (string format).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj (any): The Python object to convert to a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
