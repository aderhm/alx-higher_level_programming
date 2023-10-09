#!/usr/bin/python3
"""Defines a function."""


def is_same_class(obj, a_class):
    """ Checks if the object is exactly an instance
    of the specified class.

    Args:
        obj: instance of the class.
        a_class: the base class.

    Returns: True if the object is an instance of the specified class,
        otherwise False.
    """

    return (type(obj) is a_class)
