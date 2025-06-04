#!/usr/bin/python3
"""
1-write_file.py

This module provides a function that writes a string to a text file (UTF-8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an
        empty string.
        text (str): The string to write to the file. Defaults to an empty
        string.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If the file cannot be opened or written to.
    """
    with open(filename, 'w', encoding='utf-8') as filename:
        return filename.write(text)
