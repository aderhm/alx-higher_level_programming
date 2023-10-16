#!/usr/bin/python3
"""Defines a class Base."""

import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fields)
                for o in list_objs:
                    writer.writerow(o.to_dictionary())
    
    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                dicts = csv.DictReader(file, fieldnames=fields)
                dicts = [dict([k, int(v)] for k, v in d.items())
                         for d in dicts]
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []
