#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    length = len(my_list)
    if length == 0:
        return (None)

    for i in my_list:
        if i > max:
            max = i
    return (max)
