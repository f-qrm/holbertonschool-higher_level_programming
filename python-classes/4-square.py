#!/usr/bin/python3
"""
This module defines a Square class that represents a square.

The Square class includes size validation, encapsulation using property,
and a method to compute the area of the square.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square's sides (private).
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        Args:
            size (int, optional): The size of the square's sides.
            Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
