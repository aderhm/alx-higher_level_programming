#!/usr/bin/python3
"""Prints a text"""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ['.', '?', ':']

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in new_line_chars:
            if text[i] in new_line_chars:
                print("\n\n", end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
