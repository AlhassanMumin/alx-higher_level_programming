#!/usr/bin/python3
# 0-read_file.py
"""Defines a read file function"""

def read_file(filename=""):
    """prints a file content"""

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")        
