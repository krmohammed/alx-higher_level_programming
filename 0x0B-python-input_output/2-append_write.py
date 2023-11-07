#!/usr/bin/python3
"""
provides the function append_write()
"""


def append_write(filename="", text=""):
    """
    appends `text to `filename

    Args:
        filename: name of text file
        text (str): text to append

    Returns:
        number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
