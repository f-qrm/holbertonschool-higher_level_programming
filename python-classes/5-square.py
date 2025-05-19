#!/usr/bin/python3
"""
This module defines a Square class that represents a square by its size,
providing methods to calculate its area and to print the square using
the '#' character.
"""


class Square:
    """
    Represents a square.

    This class defines a square by its size and provides methods to calculate
    its area and print it using the '#' character.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of
            the square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The new size value to set.

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

    def my_print(self):
        """
        Prints the square using the '#' character.

        If the size is 0, it prints an empty line. Otherwise, it prints a
        square of size `size` with '#' characters.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
