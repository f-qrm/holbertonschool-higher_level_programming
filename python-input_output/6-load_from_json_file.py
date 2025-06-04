#!/usr/bin/python3
"""
6-load_from_json_file.py

This module provides a function that creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Loads and returns a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file to read from.

    Returns:
        any: The Python object represented by the JSON content.

    Raises:
        FileNotFoundError: If the file does not exist.
        JSONDecodeError: If the file contains invalid JSON.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
