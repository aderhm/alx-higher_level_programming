#!/usr/bin/python3
"""Prints a square with the character #."""


def print_square(size):
    """Prints a square with the # character.
    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
        print()
