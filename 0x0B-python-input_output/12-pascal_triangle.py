#!/usr/bin/python3
"""Defines a function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing a Pascal’s triangle.
    Args:
        n: a number.
    Rerurn:
        a list of lists of ints.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        curr_list = [1]
        tp = triangles[-1]
        for i in range(len(tp) - 1):
            curr_list.append(tp[i] + tp[i + 1])
        curr_list.append(1)
        triangles.append(curr_list)
    return triangles
