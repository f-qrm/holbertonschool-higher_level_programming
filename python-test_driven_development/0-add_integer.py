#!/usr/bin/python3
"""
This function adds two integers and returns their sum.
The second argument `b` has a default value of 98.
If either argument is not an integer or a float, a TypeError is raised.
"""
def add_integer(a, b=98):
    """
    Adds two integers a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
