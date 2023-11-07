#!/usr/bin/python3
"""
provides a BaseGeometry class
"""


class BaseGeometry:
    """
    parent class for a geometric shape
    """
    def area(self):
        """raises an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates an integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
