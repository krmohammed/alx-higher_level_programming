#!/usr/bin/python3
"""
provides the lookup() function.
"""


def lookup(obj):
    """
    provides all available attributes/methods of an object

    Args:
        obj (object): object

    Returns:
        all available attributes and methods
    """
    return dir(obj)
