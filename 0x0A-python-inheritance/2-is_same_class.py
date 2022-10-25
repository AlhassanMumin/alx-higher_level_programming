#!/usr/bin/python3
# 2-is_same_class.py

def is_same_class(obj, a_class):
    """Defines a function that returns a class instance"""
    return isinstance(obj, a_class) and a_class is not object
