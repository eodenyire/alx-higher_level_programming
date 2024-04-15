#!/usr/bin/python3
"""
A simple implementation of a Square class with comparison methods.
"""


class Square:
    """
    Represents a square with size attribute and comparison methods.
    """

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int): The size of the square's sides (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        assert isinstance(value, int), "size must be an integer"
        assert value >= 0, "size must be non-negative"
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Checks if the area of this square is less than the area of another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if the area of this square is less than or equal to the area of another square."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Checks if the area of this square is equal to the area of another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if the area of this square is not equal to the area of another square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if the area of this square is greater than the area of another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if the area of this square is greater than or equal to the area of another square."""
        return self.area() >= other.area()

