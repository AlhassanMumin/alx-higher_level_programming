#!/usr/bin/python
# 5-no_c.py

def no_c(my_string):
    """Removes all c and C"""
    a = ""
    for char in my_string:
        if char not in 'cC':
            a += char
    return a
