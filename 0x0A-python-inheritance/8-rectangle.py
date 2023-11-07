#!/usr/bin/python3
"""
provides a Square class that
inherits from BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    parent: BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

