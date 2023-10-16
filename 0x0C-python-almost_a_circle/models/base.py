#!/usr/bin/python3
"""Defines a class Base."""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
