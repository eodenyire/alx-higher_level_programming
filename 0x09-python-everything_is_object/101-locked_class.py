#!/usr/bin/python3
"""
LockedClass: A class that restricts the creation of new instance attributes.
"""


class LockedClass:
    """
    LockedClass prevents the user from dynamically creating new instance attributes,
    except for 'first_name'.
    """
    # __slots__ specifies the allowed instance attributes
    __slots__ = ["first_name"]
