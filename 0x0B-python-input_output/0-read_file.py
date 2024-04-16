#!/usr/bin/python3
"""This module to read a text file given"""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
