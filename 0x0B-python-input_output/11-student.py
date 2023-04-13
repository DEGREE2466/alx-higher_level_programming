#!/usr/bin/python3
"""Defines a Student module"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student class instance with their
        first name, last name, and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__

        return {attr: getattr(self, attr) for attr
                in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the instance Student"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

