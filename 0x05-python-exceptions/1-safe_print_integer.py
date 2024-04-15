#!/usr/bin/python3

def safe_print_integer(value):
    """
    Safely prints an integer value.

    Args:
        value: Any type of value (integer, string, etc.).

    Returns:
        True if the value is successfully printed as an integer,
        False otherwise.
    """
    try:
        # Attempt to print the value as an integer
        print("{:d}".format(value))
        return True
    except BaseException:
        # Handle any exceptions that occur during printing
        return False
