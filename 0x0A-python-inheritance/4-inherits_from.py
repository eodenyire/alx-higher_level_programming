#!/usr/bin/python3
"""Contains the inherits_from module
"""

def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass of a_class."""
    # Check if the type of obj is the same as a_class
    if type(obj) is a_class:
        return False
    # Check if the type of obj is a subclass of a_class
    return issubclass(type(obj), a_class)

