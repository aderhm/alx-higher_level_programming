#!/usr/bin/python3
"""Defines a class Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a class: Rectangle."""

    def __init__(self, width, height):
        """ Initializes """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Prints the object"""
        return ("[{}] {}/{}".format(type(self).__name__, self.__width,
                                    self.__height))
