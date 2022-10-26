#!/usr/bin/python3
# 3-to_json_string.py
"""Defines a json string functon"""

import json

def to_json_string(my_obj):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
            The number of characters written.
    """

    return json.dumps(my_obj)
