#!/usr/bin/python3
"""Defines a function."""

import json


def from_json_string(my_str):
    """From JSON string to object.
    Args:
        my_str: the JSON string.
    Rerurn:
        an object represented by a JSON string.
    """
    return (json.loads(my_str))
