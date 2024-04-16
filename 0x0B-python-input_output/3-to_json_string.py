#!/usr/bin/python3
"""Module that returns json representation of an object(string)"""
import json


def to_json_string(my_obj):
    """Function that returns the json representation of an object"""
    data = json.dumps(my_obj)
    return data
