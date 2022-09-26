#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix"""

    if matrix != [[]]:
        for row in matrix:
            row_len = len(row)
            for val in row:
                if row.index(val) < row_len - 1:
                    print("{:d} ".format(val), end="")
                else:
                    print("{:d}".format(val))
    else:
        print()
