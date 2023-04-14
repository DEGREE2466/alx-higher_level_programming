#!/usr/bin/python3
""" A class representing a geometry with an area. """


class BaseGeometry:
    """
    A class representing a geometry with an area.
    """

    def area(self):
        """
        A public instance method that is used to raise an Exception with the message
        area() is not implemented.
        """
        raise Exception("area() is not implemented")
