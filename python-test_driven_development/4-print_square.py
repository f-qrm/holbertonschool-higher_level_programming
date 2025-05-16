#!/usr/bin/python3
"""
This module defines the function print_square.
"""


def print_square(size):
    """
    Print a square made of the '#' character with the given size.
    The size parameter defines both the width and height of the square.
    Raises a TypeError if size is not an integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
