#!/usr/bin/python3
"""
provides one function, text_indentation()
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after ., ? and :

    Args:
    text (str): text to print
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if i == 0 and text[i] == ' ':
            continue
        if text[i] == ' ' and text[i - 1] in ['.', '?', ':']:
            continue
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print('\n')
