#!/usr/bin/python3
"""
provides the function is_same_class()
"""


def is_same_class(obj, a_class):
    """
    checks the instance of an object relative to
    a class

    Args:
        obj (object): the object
        a_class (class): class

    Returns:
        True is `obj is an instance of `a_class
        False otherwise
    """
    return type(obj) is a_class
