#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    i = 0
    while i < len(str):
        if (i == n):
            i += 1
            continue
        copy += str[i]
        i += 1
    return copy
