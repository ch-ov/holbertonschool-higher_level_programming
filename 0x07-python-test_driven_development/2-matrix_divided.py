#!/usr/bin/python3
""" Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Returns a new matrix """
    matrix_list = "matrix must be a matrix (list of lists) of integers/floats"
    matrix_size = "Each row of the matrix must have the same size"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_list)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(matrix_list)

        row_size = len(matrix[0])
        if row_size is not len(row):
            raise TypeError(matrix_size)

        value_matrix = []
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(matrix_list)
            value_matrix.append(round(n / div, 2))
        new_matrix.append(value_matrix)

    return new_matrix
