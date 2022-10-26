#!/usr/bin/python3
# 5-base_geometry.py
"""Defines a classGeometry with a public area instance"""

class BaseGeometry:
    """Definition of  class BaseGeometry"""
    def area(self):
        """Defines an area that raises an exception with a message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(name) != int:
            raise TypeError("width must be an integer")
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__value = abs(value)

"""Defines a Rectangle class"""

class Rectangle(BaseGeometry):
    """call BaseGeometry through constructor"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, width, height)
