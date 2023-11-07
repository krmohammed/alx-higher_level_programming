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
