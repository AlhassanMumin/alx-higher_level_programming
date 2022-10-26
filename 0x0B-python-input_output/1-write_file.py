#!/usr/bin/python3
# 1-write_file.py
"""Defines a text file line-counting function."""

def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    with open(filename, 'w', encoding="utf-8") as f:        
        num_char = f.write(text)
    return num_char
