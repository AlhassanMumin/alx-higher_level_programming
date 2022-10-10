#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
"""print a list"""
    num_elem = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_elem += 1
        except IndexError:
            print
    print()
    return num_elem
