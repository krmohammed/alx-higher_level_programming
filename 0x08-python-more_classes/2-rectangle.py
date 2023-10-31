#!/usr/bin/python3
"""
provides a rectangle class
"""


class Rectangle:
    """
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """initializes width and height

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        Returns:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """computes the area of the rectangle

        Returns:
            area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """computes the perimeter of the rectangle
            perimeter if set to 0 if either height
            or width is 0

        Returns:
            perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)
