#!/usr/bin/python3
# 6-load_from_json_file.py
"""Defines a load from json file function"""
import json


def load_from_json_file(filename):
    """Return an object creatd from json file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
