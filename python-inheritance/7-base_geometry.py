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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
