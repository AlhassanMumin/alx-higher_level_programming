#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    """print the first x elements

    args:
        my_list: the list to be printed
        x: the number of list element to print

    Return: the number of integers printed
    """
    num_int = 0

    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            num_int += 1
        except (TypeError, ValueError):
            print
    print()
    return num_int
