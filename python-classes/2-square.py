#!/usr/bin/python3
"""
This module defines a class called Square that represents a square.

It includes validation to ensure the size is a non-negative integer.
"""


class Square:
    """
    Represents a square with a given size.
    The class validates that the size is an integer and greater than or equal to 0.
    """
    def __init__(self, size = 0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
