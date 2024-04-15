#!/usr/bin/python3
"""
No module should be imported here
"""


class Square:
    """
    Defining a square by private instance size,
    instantiation with size.
    """
    def __init__(self, size):
        """
        Size : no type/value verification
        ----------------------------
        Private instance attribute size
        """
        self.__size = size
