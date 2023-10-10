#!/usr/bin/python3
"""Defines a function."""


def read_file(filename=""):
    """Reads a file and prints its content.
    Args:
        filename: the file to read.
    """

    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read())
