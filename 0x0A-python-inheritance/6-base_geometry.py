#!/usr/bin/python3
# 5-base_geometry.py
"""Defines a classGeometry with a public area instance"""


class BaseGeometry:
    """Definition of  class BaseGeometry"""
    def area(self):
        """Defines an area that raises an exception with a message"""
        raise Exception("area() is not implemented")
