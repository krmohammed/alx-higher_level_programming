#!/usr/bin/python3
"""
provides one function, add_integer()
"""


def add_integer(a, b=98):
    """
    sums two integers

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        sum of the two integers
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
