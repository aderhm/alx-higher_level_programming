#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return (None)

    max_int = 0
    for i in my_list:
        if i > max_int:
            max_int = i
    return (max_int)
