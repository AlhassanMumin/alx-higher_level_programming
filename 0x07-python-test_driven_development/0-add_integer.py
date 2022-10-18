#!/usr/bin/python3
# 3-say_my_name.py
"""
    The addition function
"""

def add_integer(a, b=98):
    """ add_integer function computes and returns sum of two integers

    Float arguments are typecasted to ints before addition is performed

    raise:
        TypeError: If either of a or b is a non-integer and non-float.
     """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
