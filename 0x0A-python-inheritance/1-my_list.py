#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MYlist"""


class MyList(list):
    """Definition  of class"""

    def print_sorted(self):
        """returns a sorted list"""
        my_list = []
        for idx in range(len(self)):
            my_list.append(list.__getitem__(self, idx))
        my_list.sort()
        print(my_list)
