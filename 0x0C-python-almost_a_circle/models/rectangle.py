#!/usr/bin/python3
"""
Provides the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class

    Parent:
        Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes attributes of Rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y setter
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        computes the area of the rectangle

        Returns:
            area value of Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {\
                self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        updates `self

        Args:
            args (list): no-keyword argument
            kwargs (dict): key-worded argument
        """
        if len(args) > 0:
            props = ['id', 'width', 'height', 'x', 'y']
            for ind, k in enumerate(args):
                setattr(self, props[ind], k)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        provides the dict rep of of `self

        Returns:
            the dictionary representation of `self
        """
        return {
                'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x,
                'y': self.y
                }
