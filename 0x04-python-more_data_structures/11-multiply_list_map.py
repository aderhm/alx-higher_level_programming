#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    two_times_list = list(map(lambda x: x * number, my_list))
    return (two_times_list)
