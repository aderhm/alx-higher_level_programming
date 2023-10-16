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
