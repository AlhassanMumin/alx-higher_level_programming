#!/usr/bin/python3
# 9-max_integer.py
def max_integer(my_list=[]):
    """maximum integer"""

    if len(my_list) == 0:
        return None
    my_list.sort()
    return my_list[len(my_list) - 1]
