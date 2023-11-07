#!/usr/bin/python3
"""
provides the read_file() function
"""


def read_file(filename=""):
    """
    reads a text file and prints to stdout

    Args:
        filename (str): name of text file
    """
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read())
