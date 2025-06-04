#!/usr/bin/python3
"""
Module for serializing and deserializing data to/from a JSON file.
"""


import json
def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python object and saves it to a JSON file.

    This function converts a Python object (e.g., list, dict) to a JSON-formatted
    string and writes it to a specified file.

    Args:
        data (any): The Python data structure to serialize (e.g., dict, list).
        filename (str): The name of the file where the data will be saved.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
def load_and_deserialize(filename):
    """
    Loads data from a JSON file and deserializes it into a Python object.

    This function reads a JSON-formatted file and converts it back into
    a corresponding Python data structure (e.g., dict, list).

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        any: The Python object resulting from the deserialization of the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
