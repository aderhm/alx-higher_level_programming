#!/usr/bin/python3
"""Defines a function."""


def lookup(obj):
    """ Returns the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """

    return dir(obj)
