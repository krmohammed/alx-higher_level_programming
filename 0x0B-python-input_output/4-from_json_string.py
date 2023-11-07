#!/usr/bin/python3
"""
provides the function from_json_string()
"""


import json


def from_json_string(my_str):
    """
    deserializes `my_str

    Args:
        my_str: JSON string

    Returns:
        object represented by JSON string
    """
    return json.loads(my_str)
