#!/usr/bin/python3
"""Magic Class doing exactly as the Python bytecode"""
import math


class MagicClass:
    """
    MagicClass from a bytecode
    """
    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area of a circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """circumference of a circle"""
        return 2 * math.pi * self.__radius
