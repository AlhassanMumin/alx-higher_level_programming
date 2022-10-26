#!/usr/bin/python3
# 2-append_write.py
"""Defines a function that appends a text"""


def append_write(filename="", text=""):
    """Print a given number of lines from a UTF8 text file to stdout.
    Args:
        filename (str): The name of the file.
        nb_lines (int): The number of lines to read from the file.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        num_app = f.write(text)
    return num_app
