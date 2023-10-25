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
        creates the size parameter

        Args:
            size (int): size of square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """size attribute's getter function

        Returns:
            the value of size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns:
            the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
