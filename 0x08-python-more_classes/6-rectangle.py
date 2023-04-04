#!/usr/bin/python3
"""Define a rectangle"""

class Rectangle:
    """Represents rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    
    @property
    def width(self):
        """Get/set the height of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get/set the width of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """calculates the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        
            return 2 * (self.width + self.height)

    def __str__(self):
        '''Returning the string representation of the rectangle'''
        if self.width == 0 or self.height == 0:
            return rectangle
        
            for i in range(self.height - 1):
                rectangle += "#" * self.width + "\n"
            rectangle += "#" * self.width
            return rectangle

    def __repr__(self):
        """creating a recreation of the instance call"""
        rep = "{}({}, {})".format(self.__class__.__name__,
                                  self.width, self.height)
        return rep
    del __del__(self):
        """
            Printing a message with instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
