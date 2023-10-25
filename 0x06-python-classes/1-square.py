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
    def __init__(self, size):
        """
        creates the paramaters for each instance of this class

        Args:
            size (int): size of square
        """
        self.__size = size
