#!/usr/bin/python3
# 6-print_sorted_dictionary.py
def print_sorted_dictionary(a_dictionary):
    """sort a dictionary in ordered keys"""

    for x, y in sorted(a_dictionary.items()):
        print("{}: {}".format(x, y))
