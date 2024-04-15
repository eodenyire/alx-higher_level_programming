#!/usr/bin/python3
"""
No module should not be imported
"""


class Square:
    """
    Private instance attribute size
    public instance method
    """

    def __init__(self, size=0):
        """
        Private instance attribute
        Parameters
        -------------------------
        size : integer else TypeError
            If size is less than 0, raise ValueError
        """
        self.__size = size

    @property
    def size(self):
        """
        To retrieve private instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        To set private instance attribute
        """
        self.__size = value
        try:
            assert isinstance(value, int)
        except AssertionError:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Public instance method
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print square using #
        """
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print()
