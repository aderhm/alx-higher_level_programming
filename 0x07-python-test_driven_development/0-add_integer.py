#!/usr/bin/python3
"""Adds two integers."""


def add_integer(a, b=98):
    """Return the addition of a and b.
    Float arguments are typecasted to ints before performing the addition.
    Raises:
        TypeError: If either a or b is a non-integer and non-float value.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
