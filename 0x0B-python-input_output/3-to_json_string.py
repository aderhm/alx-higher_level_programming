#!/usr/bin/python3
"""Defines a function."""


import json

def to_json_string(my_obj):
    """Treats the JSON representation of an object (string):
    Args:
        my_obj: the object.
    Rerurn:
        the JSON representation of the object.
    """
    return (json.dumps(my_obj))
