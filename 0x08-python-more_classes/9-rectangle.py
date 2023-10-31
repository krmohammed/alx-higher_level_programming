#!/usr/bin/python3
"""
provides a rectangle class
"""


class Rectangle:
    """
    defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes width and height

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares the area of two rectangles

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Returns:
            biggest rectangle (based on area)
            rect_1 if both are of the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """creates a rectangle
            special type of rectangle => square

        Args:
            size (int): size of the square

        Returns:
            new rectangle instance (square)
        """
        return cls(size, size)

    def __str__(self):
        str_rep = ''
        if self.__height == 0 or self.__width == 0:
            return str_rep
        for i in range(self.__height):
            for j in range(self.__width):
                str_rep += str(self.print_symbol)
            str_rep += '\n'
        return str_rep.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
