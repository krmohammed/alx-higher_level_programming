#!/usr/bin/python3
"""
provides the function to_json_string()
"""


import json

def to_json_string(my_obj):
    """
    serializes `my_obj

    Args:
        my_obj: object

    Returns:
        JSON representation of `my_obj
    """
    return json.dumps(my_obj)
