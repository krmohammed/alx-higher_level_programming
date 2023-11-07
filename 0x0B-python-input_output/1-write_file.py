#!/usr/bin/python3
"""
provides the write_file() function
"""


def write_file(filename="", text=""):
    """
    writes `text to `filename

    Args:
        filename: text file
        text (str): text to write

    Returns:
        number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
