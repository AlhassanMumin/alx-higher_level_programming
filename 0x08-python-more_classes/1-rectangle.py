#!/usr/bin/python3
# 1-rectangle.py
"""Defines a Rectangle class."""


class Rectangle:
    """the rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

