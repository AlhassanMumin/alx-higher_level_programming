#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """squares elements of a matrix"""

    new_matrix = []

    for row in matrix:
        new_matrix += [list(map(lambda x: x**2, row))]

    return new_matrix
