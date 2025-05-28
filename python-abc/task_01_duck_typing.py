#!/usr/bin/env python3
"""
This module defines an abstract base class `Shape` and two concrete
subclasses: `Circle` and `Rectangle`.

The `Shape` class enforces a structure requiring all shapes to implement
methods to compute both area and perimeter.

Subclasses:
    - Circle: Represents a circle and calculates area and perimeter using
    its radius.
    - Rectangle: Represents a rectangle and calculates area and perimeter
    using its width and height.

There is also a helper function `shape_info` that takes a shape instance
and prints its area and perimeter.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    All subclasses must implement the `area` and `perimeter` methods.
    """
    @abstractmethod
    def area(self):
        """
        Compute the area of the shape.

        This method must be overridden in any subclass.

        Returns:
            float: Area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of the shape.

        This method must be overridden in any subclass.

        Returns:
            float: Perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape defined by its radius.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return (self.radius * 2) * pi


class Rectangle(Shape):
    """
    Rectangle shape defined by its width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(forme):
    """
    Print the area and perimeter of any object that implements
    area() and perimeter() methods.

    Args:
        forme: Any object with area() and perimeter() methods.
    """
    print("Area: {}".format(forme.area()))
    print("Perimeter: {}".format(forme.perimeter()))
