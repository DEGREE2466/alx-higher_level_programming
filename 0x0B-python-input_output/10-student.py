#!/usr/bin/python3
"""A function that defines a student class"""


class Student:
    """Represent a Class student"""

    def __init__(self, first_name, last_name, age):
        """Use to Initialize a new Student instance
        with the given student name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation
        of this instance Student"""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr
                in attrs if hasattr(self, attr)}
