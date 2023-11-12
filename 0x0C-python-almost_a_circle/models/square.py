#!/usr/bin/python3
"""
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
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
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
