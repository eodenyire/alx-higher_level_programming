#!/usr/bin/python3
"""

This module contains a function that adds two numbers.

"""


def add_integer(a, b=98):
    """
    Adds two integer and/or float numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The addition of the two given numbers.

    Raises:
        TypeError: If 'a' or 'b' are not integer and/or float numbers.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
