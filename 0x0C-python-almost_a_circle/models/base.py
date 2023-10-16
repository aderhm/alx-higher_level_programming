#!/usr/bin/python3
"""Defines a class Base."""


class Base:
    """Represents a class: Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Init instances """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects