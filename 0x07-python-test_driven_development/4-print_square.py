#!/usr/bin/python3
"""
provides one function, print_square()
"""


def print_square(size):
    """
    prints a square

    Args:
        size (int): size of the square
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        print('#' * int(size))
