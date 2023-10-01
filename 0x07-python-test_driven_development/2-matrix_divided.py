#!/usr/bin/python3
"""Divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float): divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div == 0.
    Returns:
        A new matrix representing the result of the division.
    """
    divided_matrix = []

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        for i in lst:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    if not all(len(lst) == len(matrix[0]) for lst in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    divided_matrix = [
        list(map(lambda x: round(x / div, 2), row)) for row in matrix
        ]

    return (divided_matrix)
