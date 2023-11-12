#!/usr/bin/python3
"""
Provides the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class

    Parents:
        Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes attributes of Rectangle class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates `self

        Args:
            args (list): no-keyword argument
            kwargs (dict): key-worded argument
        """
        if len(args) > 0:
            props = ['id', 'size', 'x', 'y']
            for k, v in enumerate(args):
                setattr(self, props[k], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def to_dictionary(self):
        """
        provides the dict rep of of `self

        Returns:
            the dictionary representation of `self
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
