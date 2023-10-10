#!/usr/bin/python3
"""Defines a function."""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file (UTF8)
    Args:
        my_obj: the JSON string.
        filename: the file to write to.
    Rerurn:
        an object represented by a JSON string.
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
