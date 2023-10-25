#!/usr/bin/python3
"""
Defines a square class
"""


class Square:
    """
    Square class initializes size attribute privately

    Attributes:
        no public attribute
    """
    def __init__(self, size=0):
        """
        creates the size parameter with validation

        Args:
            size (int): size of square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
