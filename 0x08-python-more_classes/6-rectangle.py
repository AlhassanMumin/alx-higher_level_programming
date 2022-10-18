#!/usr/bin/python3
# 6-rectangle.py
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0") 
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)

    def __str__(self):
        """returns a printable representation of the rectangle"""
        self.__stri = ""
        for char in range(self.__height):
            for symb in range(self.__width):
                if symb == self.__width - 1:
                    if char != self.__height - 1:
                        self.__stri += "#\n"
                    else:
                        self.__stri += "#"
                else:
                    self.__stri += "#"
        return self.__stri

    def __repr__(self):
        """returins a string representation of the rectangle"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """deletes a rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
