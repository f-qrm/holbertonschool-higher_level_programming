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
