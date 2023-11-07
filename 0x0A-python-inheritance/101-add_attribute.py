#!/usr/bin/python3j
"""
provides the function add_attribut()
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object

    Args:
        obj: object to add attribute
        name (str): name of attribute
        value (any): attribute value
    """
    if not hasattr(obj, name):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

