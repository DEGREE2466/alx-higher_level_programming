#!/usr/bin/python3
"""A Module containing the Student class"""


class Student:
    """The class that represents each student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Instance Student"""
        return self.__dict__
