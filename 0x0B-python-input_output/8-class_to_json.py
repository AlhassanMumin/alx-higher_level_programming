#!/usr/bin/python3
# 8-class_to_json.py
""" dictionary description with simple data structure"""

def class_to_json(obj):
     """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
