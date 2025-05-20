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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle.
            Defaults to 0.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        Calculate and return the area of the rectangle.
        The area is computed as width multiplied by height.
        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        The perimeter is computed as 2 times the sum of width and height.
        If either width or height is 0, the perimeter is 0.
        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """

        if (self.width == 0) or (self.height == 0):
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return the string representation of the rectangle using the '#'
        character.

        This method constructs a visual representation of the rectangle by
        generating a string consisting of lines of '#' characters. The number
        of lines corresponds to the rectangle's height, and each line contains
        '#' repeated according to the rectangle's width.

        If either the width or height of the rectangle is 0, an empty
        string is returned.
        Returns:
            str: A string representing the rectangle with '#' characters,
            or an
                empty string if width or height is 0.
        Example:
            For a rectangle with width=4 and height=3, this method returns:
            ####
            ####
            ####
        """
        if (self.width == 0) or (self.height == 0):
            return ""
        lines = []
        for i in range(self.height):
            lines.append(str(self.print_symbol) * self.width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle that can be used
        to recreate a new instance using eval().

        The returned string is in the format: Rectangle(width, height)

        Returns:
            str: A string that represents a valid Python expression to
                create an identical Rectangle instance.
        Example:
            >>> r = Rectangle(4, 6)
            >>> repr(r)
            'Rectangle(4, 6)'
            >>> r2 = eval(repr(r))
            >>> print(r2)
            ####
            ####
            ####
            ####
            ####
            ####
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Detect instance deletion and print a message.

        This method is called when an instance of Rectangle
        is about to be destroyed
        (garbage collected). It prints the message "Bye rectangle..."
        to notify that the instance is being deleted.

        Note:
            This method helps track the deletion of Rectangle
            instances and can be
            useful for debugging or cleanup purposes.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """
        Compare deux rectangles et retourne celui qui a la plus grande aire.
        Si les aires sont égales, retourne rect_1.

        Args:
            rect_1 (Rectangle): Le premier rectangle.
            rect_2 (Rectangle): Le second rectangle.

        Raises:
            TypeError: Si rect_1 ou rect_2 n'est pas une instance de Rectangle.

        Returns:
            Rectangle: Le rectangle avec la plus grande aire ou rect_1
            si égalité.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Crée un nouveau rectangle carré avec largeur et hauteur égales.

        Args:
            size (int): La taille du côté du carré (largeur et hauteur).
            Par défaut 0.

        Returns:
            Rectangle: Une nouvelle instance de Rectangle où
            width == height == size.

        Exemple:
            >>> square = Rectangle.square(5)
            >>> print(square.width)
            5
            >>> print(square.height)
            5
        """
        return cls(size, size)
