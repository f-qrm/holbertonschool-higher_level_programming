#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

It includes size validation and a method to compute the square's area.
"""


class Square:
    """
    Represents a square with a specific size.

    This class allows the creation of square objects with a given size and
    provides a method to compute the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size multiplied by itself).
        """
        return self.__size * self.__size
