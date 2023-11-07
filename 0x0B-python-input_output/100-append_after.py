#!/usr/bin/python3
"""
provides the function append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts `new_string on a new line
    after the line containing `search_string

    Args:
        filename: name of text file
        search_string (str): string to look out for
        new_string (str): inserting string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in all_lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
