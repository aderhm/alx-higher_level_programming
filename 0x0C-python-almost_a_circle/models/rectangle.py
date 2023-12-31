#!/usr/bin/python3
"""Defines a class Rectangle.
inheritance of class Base
"""

from models.base import Base


class Rectangle(Base):
    """Represents a class: Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
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
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        a = 0
        while a < self.y:
            print()
            a += 1
        for i in range(0, self.height):
            b = 0
            while b < self.x:
                print(" ", end='')
                b += 1
            for j in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ str """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args and len(args):
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        attrs = ['id', 'width', 'height', 'x', 'y']
        rectangle_dict = {}

        for item in attrs:
            rectangle_dict[item] = getattr(self, item)

        return rectangle_dict
