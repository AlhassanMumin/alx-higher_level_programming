#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    """multiply a dictionary value by 2"""
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value*2

    return new_dictionary
