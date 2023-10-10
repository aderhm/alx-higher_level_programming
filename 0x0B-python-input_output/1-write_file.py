#!/usr/bin/python3
"""Defines a function."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename: the file to write to.
        text: the text to be written.
    Rerurn:
        the number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write("{}".format(text))
    return (len(text))
