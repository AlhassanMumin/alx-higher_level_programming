#!/usr/bin/python3
# 4-print_square.py
"""Defines a print square function"""

def print_square(size):
    """It print a square in 2-D

    raises:
        TypeError: if size  is not an integer
    raises:
        ValueEerrpr: if size is less than 0
    """
 
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and  size < 0:
        raise TypeError("size must be an integer")

    for pound in range(size):
        for char in range(size):
            print("#", end="")
        print()
