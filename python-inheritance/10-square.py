#!/usr/bin/python3
"""
This module defines the BaseGeometry class with a placeholder method.

The class is designed to serve as a base for geometry-related classes.
It contains a method `area` that is intended to be overridden in subclasses.
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometric shapes.

    It defines a method `area` which should be implemented by
    any subclass that inherits from it. Calling `area()` directly
    will raise an Exception, indicating that the method is not implemented.
    """
    def area(self):
        """
        Raises an Exception to indicate that the method is not implemented.

        This method should be overridden in subclasses that define
        specific geometry (e.g., Rectangle, Circle).

        Raises:
            Exception: Always raises "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Args:
            name (str): The name of the value (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry and represents a rectangle.

    It uses integer_validator to ensure width and height are valid
    integers > 0.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square.

    Since all sides of a square are equal, it passes the same value
    twice to the Rectangle constructor.
    """

    def __init__(self, size):
        """
        Initializes a square with validated size.

        Args:
            size (int): The size of the square's sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area (size * size)
        """
        return self.__size * self.__size
