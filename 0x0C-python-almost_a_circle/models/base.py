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

    @classmethod
    def save_to_file(cls, list_objs):
        """ rites the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        dicts = []

        if list_objs is None:
            pass
        else:
            for i in range(0, len(list_objs)):
                dicts.append(list_objs[i].to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        else:
            inst = cls(2)
        inst.update(**dictionary)
        return inst
