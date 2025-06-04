#!/usr/bin/python3
"""
5-save_to_json_file.py

This module provides a function that writes an object to a text file using
JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using its JSON representation.

    Args:
        my_obj (any): The Python object to be serialized.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
