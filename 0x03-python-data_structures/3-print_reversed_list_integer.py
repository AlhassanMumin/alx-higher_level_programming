#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """print the element in the reverse  order"""

    if isinstance(my_list, list):
        my_list.reverse()
        for integer in my_list:
            print("{:d}".format(integer))
