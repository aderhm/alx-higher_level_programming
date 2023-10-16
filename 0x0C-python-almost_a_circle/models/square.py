#!/usr/bin/python3
"""Defines a class Square.
inheritance of class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class: Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Init instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args):
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        attrs = ['id', 'size', 'x', 'y']
        rectangle_dict = {}

        for item in attrs:
            rectangle_dict[item] = getattr(self, item)

        return rectangle_dict
