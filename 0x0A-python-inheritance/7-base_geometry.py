#!/usr/bin/python3
"""
A module that defines the class BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry class that is an empty
    """

    def area(self):
        """
        A public instance method that raises the Exception with
        the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value:
        * you can assume name is always a string
        * if value is not an integer: raise a TypeError exception, with
        the message <name> must be an integer
        * if value is less or equal to 0: raise a ValueError exception with
        the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
