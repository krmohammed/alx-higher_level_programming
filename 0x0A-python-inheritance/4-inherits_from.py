#!/usr/bin/python3
"""
provides the function inherits_from()
"""


def inherits_from(obj, a_class):
    """
    checks for inheritance and not strict instance

    Args:
        obj (object): object
        a_class (class): class

    Returns:
        True if inherited, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
