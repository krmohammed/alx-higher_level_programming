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

    def area(self):
        """computes the area of the rectangle
        """
        return self.__width * self.__height

    def __repr__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
