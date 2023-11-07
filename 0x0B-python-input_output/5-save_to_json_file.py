#!/usr/bin/python3
"""
provides the save_to_json_file() function
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes `my_obj to `filename

    Args:
        my_obj: object
        filename: name of text file

    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
