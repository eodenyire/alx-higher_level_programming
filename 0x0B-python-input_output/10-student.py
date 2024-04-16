#!/usr/bin/python3
"""
Module contains the Student class
"""


class Student:
    """Defining a student
    """
    def __init__(self, first_name, last_name, age):
        """Instanciates and initializes 
        the student attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary
           representation of a Student
           instance
        """
        my_dict = {}
        if attrs is None:
            return self.__dict__

        for attr in attrs:
            try:
                my_dict[attr] = self.__dict__[attr]
            except KeyError:
                pass
        return my_dict
