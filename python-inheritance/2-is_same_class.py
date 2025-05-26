#!/usr/bin/python3
"""
This module contains a function to check if an object
is **exactly** an instance of a given class,
without considering inheritance.

The function returns True if the object is a direct instance
of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an exact instance of a given class.

    Args:
        obj (any): The object to test.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is a direct instance of `a_class`,
              False otherwise (even if `obj` is an instance of a subclass).

    Example:
        >>> class Animal:
        ...     pass
        >>> class Dog(Animal):
        ...     pass
        >>> rex = Dog()
        >>> is_exact_instance(rex, Dog)
        True
        >>> is_exact_instance(rex, Animal)
        False
    """
    return type(obj) is a_class
