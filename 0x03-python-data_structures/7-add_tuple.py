#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """add two tuples"""

    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    tuple_sum_1stVal = tuple_a[0] + tuple_b[0]
    tuple_sum_2ndVal = tuple_a[1] + tuple_b[1]
    tuple_resultant = tuple_sum_1stVal, tuple_sum_2ndVal

    return tuple_resultant
