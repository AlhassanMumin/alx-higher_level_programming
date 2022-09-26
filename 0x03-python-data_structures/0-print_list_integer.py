#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """prints all integers in my_list"""
    for integer in range(len(my_list)):
        print("{:d}".format(my_list[integer]))
