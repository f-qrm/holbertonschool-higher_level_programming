#!/usr/bin/python3
"""
This module defines the function say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints a full name based on the given arguments.
    Raises a TypeError if either argument is not a string.
    Displays: My name is <first_name> <last_name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
