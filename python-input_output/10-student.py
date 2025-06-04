#!/usr/bin/python3
"""
10-student.py

This module defines a Student class with attributes and a method to retrieve
a dictionary representation of the instance, optionally filtered by a list of
attributes.
"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes included in
        the list and present in the instance dictionary are returned.

        Args:
            attrs (list, optional): List of attribute names to include in the
                                    returned dictionary. Defaults to None.

        Returns:
            dict: Dictionary containing the requested attributes of the
            student,
                  or all attributes if attrs is None or not a list.
        """
        if isinstance(attrs, list):
            new_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return new_dict
        else:
            return self.__dict__
