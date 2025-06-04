#!/usr/bin/python3
"""
0-read_file.py

This module contains a function that reads a text file (UTF-8) and
prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs during reading.
    """
    with open(filename, encoding='utf-8') as filename:
        cont = filename.read()
        print(cont, end="")
