#!/usr/bin/python3
"""
2-append_write.py

This module provides a function that appends a string to the end of a text
file (UTF-8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and returns the number
    of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty
        string.
        text (str): The string to append to the file. Defaults to an empty
        string.

    Returns:
        int: The number of characters written.

    Raises:
        IOError: If the file cannot be opened or written to.
    """
    with open(filename, 'a', encoding='utf-8') as filename:
        return filename.write(text)
