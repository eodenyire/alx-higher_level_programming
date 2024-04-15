#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Safely divides two integers and prints the result.

    Args:
        a: The numerator (integer).
        b: The denominator (integer).

    Returns:
        The result of the division, or None if division by zero occurs.
    """
    div = 0  # Initialize the division result
    try:
        # Attempt the division
        div = a / b
        return div
    except BaseException:
        # Handle division by zero or any other exceptions
        div = None
        return None
    finally:
        # Print the result of the division, whether successful or not
        print("Inside result: {}".format(div))
