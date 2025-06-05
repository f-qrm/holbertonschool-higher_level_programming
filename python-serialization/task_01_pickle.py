#!/usr/bin/env python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""


import pickle
class CustomObject:
    """
    A class representing a custom object with basic attributes and
    methods for serialization and deserialization.
    """

    def __init__(self, name:str, age: int, is_student: bool):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    def display(self):
        """
        Display the attributes of the CustomObject instance.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
    def serialize(self, filename):
        """
        Serialize the object and save it to a file using pickle.

        Args:
            filename (str): The name of the file to save the serialized object to.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None
    @classmethod
    def deserialize(cls, filename):
        """
        Load and deserialize a CustomObject instance from a file using pickle.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object if successful, or None on failure.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
