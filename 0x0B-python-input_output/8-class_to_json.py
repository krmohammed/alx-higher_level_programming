#!/usr/bin/python3
"""
provides the function class_to_json()
"""
import json


def class_to_json(obj):
    """
    serializes the dictionary description
    of the class object `obj

    Args:
        obj: class object

    Returns:
        serialized dict
    """
    return obj.__dict__
