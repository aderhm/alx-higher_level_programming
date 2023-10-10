#!/usr/bin/python3
"""Defines a function."""

import json


def load_from_json_file(filename):
    """loads from a JSON file.
    Args:
        filename: the file to read from.
    Rerurn:
        an object.
    """
    with open(filename) as myFile:
        return (json.load(myFile))
