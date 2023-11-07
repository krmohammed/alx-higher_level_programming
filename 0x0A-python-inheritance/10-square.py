#!/usr/bin/python3
"""
provides a Square class that
inherits from the Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    parent: Rectangle class
    """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """computes the area of the rectangle
        """
        return self.__size ** 2
