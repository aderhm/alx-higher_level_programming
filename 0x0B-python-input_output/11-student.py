#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a class: Student"""

    def __init__(self, first_name, last_name, age):
        """Inits"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
