#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return new_dict
        else:
            return self.__dict__

