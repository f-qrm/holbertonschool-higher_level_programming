#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes.
"""


class Square:
    """
    Represents a square defined by size and position.

    Attributes:
        __size (int): size of the square
        __position (tuple): position offset for printing the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size (int): size of the square's sides
            position (tuple): tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using '#' and considering the position.
        """
        if self.size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.size):
            print(" " * self.__position[0] + "#" * self.__size)
