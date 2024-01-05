#!/usr/bin/python3
"""Module: finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    s = 0
    e = len(list_of_integers) - 1

    while s < e:
        mid = (s + e) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            e = mid
        else:
            s = mid + 1

    return list_of_integers[s]
