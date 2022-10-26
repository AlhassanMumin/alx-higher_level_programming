#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a JSON-to-object function."""
import json

def from_json_string(my_str):
    """
    this function will make  use of json load method
    Args:
        my_str the object passed
    Return:
            the Python object representation of a JSON string.

    """ 
    return json.loads(my_str)
