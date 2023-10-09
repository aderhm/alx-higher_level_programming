#!/usr/bin/python3
"""Defines a class MyList."""


class MyList(list):
    """ Represents a list.
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Prints the sorted list """
        sortedList = self.copy()
        sortedList.sort()
        print(sortedList)
