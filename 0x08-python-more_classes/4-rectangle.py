#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiates a rectangle with optional width and height"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        perimeter = 0
        if self.__height != 0 or self.__width != 0:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter

    def __str__(self):
        """Returns a string representation of the rectangle with '#'"""
        str_ = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            if i < (self.__height - 1):
                str_ += ("#" * self.__width) + "\n"
            else:
                str_ += ("#" * self.__width)
        return str_

    def __repr__(self):
        """Returns a string representation of the rectangle object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

