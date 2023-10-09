#!/usr/bin/python3
"""Defines a class Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a class: Square."""

    def __init__(self, size):
        """ Initializes """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns sqaure area"""
        return (self.__size ** 2)
