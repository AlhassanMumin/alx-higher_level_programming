#!/usr/bin/python3
# 5-base_geometry.py
"""Defines a classGeometry with a public area instance"""

class BaseGeometry:
    """Definition of  class BaseGeometry"""
    def area(self):
        """Defines an area that raises an exception with a message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.__value = value


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
