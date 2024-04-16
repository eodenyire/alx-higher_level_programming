#!/usr/bin/python3
"""Module that returns python data structure"""
import json


def from_json_string(my_str):
    """Function that returns an object(Python data structure)
    represented by a json string"""
    data = json.loads(my_str)
    return data
