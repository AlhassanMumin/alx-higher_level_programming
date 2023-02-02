#!/usr/bin/python3
# square a matrix

def square_matrix_map(matrix=[]):
    """square the matrix"""

    res = []

    for List in matrix:
        res.append(list(map((lambda x: x * x), List)))
    return res
