#!/usr/bin/python3
"""Defines a function."""


def inherits_from(obj, a_class):
    """ Checks if the object is an instance
    of the specified class.

    Args:
        obj: instance of the class.
        a_class: the base class.

    Returns: True if the object is an instance of the specified class,
        otherwise False.
    """

    if type(obj) is a_class:
        return False
    return (isinstance(obj, a_class))
