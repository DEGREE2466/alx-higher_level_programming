#!/usr/bin/python3
"""
A Module that defines the class BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry that is empty
    """

    def area(self):
        """
        A public instance method that raises an Exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A public instance method that validates value:
        * you can assume name is always a string
        * if value is not an integer: raise a TypeError exception, with the
        message <name> must be an integer
        * if value is less or equal to 0: raise a ValueError exception with
        the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Public instance method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Print and return the following rectangle description:
        Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
