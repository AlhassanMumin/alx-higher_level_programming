#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix function"""

def matrix_divided(matrix, div):
    """returns a new matrix
    Must contain only float and integer elements

    raise:
        TypeError:when a matrix is not a list of lists of integers/floats

    raises:
        ZeroDivisionError: when the div is zero
    """

    for sub_list in matrix:
        if not  isinstance(sub_list, list):
            raise TypeError("matrix must be a matrix (list of lists)\
                            of integers/floats")
        else:
            for value in sub_list:
                if type(value) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) \
                                    of integers/floats")
    mat_len = len(matrix)
    for row_len in range(mat_len - 1):
        if len(matrix[row_len]) != len(matrix[row_len + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_mat = [[round((val / div), 2) for val in lis] for lis in matrix]

    return new_mat
