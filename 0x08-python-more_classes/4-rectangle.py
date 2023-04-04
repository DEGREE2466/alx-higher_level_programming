#!/usr/bin/python3
"""Define a rectangle"""

class Rectangle:
    """
    Represents rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args: 
            width (int): The width of the new rectangle.
            height(int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Get/set the height on the rectangle."""
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
        """Get/set the height of the rectangle"""
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
        """Calculates the perimeter of a rectangle"""
        return 2 * (self.width + self.height) if self.width != 0 and self.height != 0 else 0
    
    def __str__(self):
        """
            Returning the string representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.height):
                rectangle += "#" * self.width
                if i != self.height - 1:
                    rectangle += "\n"
            return rectangle
    
    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)
