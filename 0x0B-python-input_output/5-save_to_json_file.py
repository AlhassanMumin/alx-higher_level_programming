#!/usr/bin/python3
# 5-save_to_json_file.py
"""Defines a save to json file function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, 'w' , encoding="utf-8") as f:
        json.dump(my_obj, f)
