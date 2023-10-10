#!/usr/bin/python3
"""Defines a function."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8)
    Args:
        filename: the file to write to.
        text: the text to be appended.
    Rerurn:
        the number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as myFile:
        myFile.write("{}".format(text))
    return (len(text))
