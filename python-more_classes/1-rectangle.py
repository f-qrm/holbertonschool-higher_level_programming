#!/usr/bin/python3
"""This module defines a class named Rectangle.

The Rectangle class is an empty class that represents a geometric rectangle.
It serves as a foundation for learning about classes and object-oriented
programming in Python.
"""


class Rectangle:
    """Represents a rectangle defined by width and height.
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    Methods:
        __init__(self, width=0, height=0): Initializes the Rectangle instance.
        width(self): Retrieves the width of the rectangle.
        width(self, value): Sets the width, validating the value.
        height(self): Retrieves the height of the rectangle.
        height(self, value): Sets the height, validating the value.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        Args:
            value (int): The new width value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        Returns:
            int: The current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Args:
            value (int): The new height value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
