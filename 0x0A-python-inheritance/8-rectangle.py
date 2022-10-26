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
    """Intialize a new Rectangle.
    Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
    """

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
