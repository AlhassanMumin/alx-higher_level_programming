#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """print the element in the reverse  order"""

    if isinstance(my_list, list):
        list_range = len(my_list) - 1
        for integer in range(list_range, -1, -1):
        print("{:d}".format(my_list[integer]))
