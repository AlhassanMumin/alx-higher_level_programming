#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """numbers divisible by two"""

    new_list = []
    for indx, val in enumerate(my_list):
        if val % 2 == 0:
            new_list.insert(indx, True)
        else:
            new_list.insert(indx, False)
    return new_list
