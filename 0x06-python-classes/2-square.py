#!/usr/bin/python3
"""
No module should be imported here
"""


class Square:
    """
    Defining a square by private attribute size,
    and instantiation with optional size:
    def __init__(self, size=0):
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
