#!/usr/bin/python3
"""
No module should be imported here
"""


class Square:
    """
    Private instance attribute size and public instance method
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
