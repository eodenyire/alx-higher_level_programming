#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    Private instance attribute size
    public instance method
    """

    def __init__(self, size=0):
        """private instance attribute
        parameters
        -------------------------
        size : integer else TypeError
        if size less than 0, raise value error
        """
        self.__size = size

    @property
    def size(self):
        """
        to retrieve private instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        to set private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        public instance method
        returns the current square area
        """
        return self.__size ** 2
