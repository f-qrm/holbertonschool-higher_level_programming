#!/usr/bin/python3
"""
4-from_json_string.py

This module provides a function that returns a Python object
represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a corresponding Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
