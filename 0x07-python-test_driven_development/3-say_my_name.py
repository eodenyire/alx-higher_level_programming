#!/usr/bin/python3
"""

This script defines a function to output a personalized message

"""


def say_my_name(first_name, last_name=""):
    """ Prints a formatted message with the provided names

    Args:
        first_name: The first name
        last_name: The last name (default is an empty string)

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
