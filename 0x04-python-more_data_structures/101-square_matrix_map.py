#!/usr/bin/python3
# square a matrix

def square_matrix_map(matrix=[]):
    """square the matrix"""

    res = list(map((lambda x: list(map((lambda y: y * y), x))), matrix))
    return res
