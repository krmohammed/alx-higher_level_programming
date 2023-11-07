#!/usr/bin/python3
"""
provides the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    checks for instance flexibly

    Args:
        obj (object): object to check
        a_class (class): class to compare

    Returns:
        True if isinstance otherwise, False
    """
    return isinstance(obj, a_class)
