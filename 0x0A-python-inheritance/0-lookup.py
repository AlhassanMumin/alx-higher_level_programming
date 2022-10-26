#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function."""

def lookup(obj):
    """
    The lookup function returns a list of attributes and method

    Args:
        obj: the object passed
    Return:
            a list of an object's available attributes.
    """
    return dir(obj)
