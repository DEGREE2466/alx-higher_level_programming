#!/usr/bin/python3
"""
A Module that defines the Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The class Rectangle that inherits from a BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes an instance of Rectangle with width and height
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
