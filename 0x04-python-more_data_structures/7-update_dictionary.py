#!/usr/bin/python3
# 7-update_dictionary.py

def update_dictionary(a_dictionary, key, value):
    """updates a dictionary"""

    if key in a_dictionary:
        a_dictionary[key] = value
    elif key not in a_dictionary:
        a_dictionary[key] = value

    return a_dictionary
