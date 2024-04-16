#!/usr/bin/python3
"""This module creates an object from a json file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object
    from a json file"""
    with open(filename, "r") as f:
        return json.load(f)
