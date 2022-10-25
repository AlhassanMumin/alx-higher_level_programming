#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MYlist"""


class MyList(list):
    """Definition  of class"""

    def print_sorted(self):
        """returns a sorted list"""
        return print(sorted(self))
