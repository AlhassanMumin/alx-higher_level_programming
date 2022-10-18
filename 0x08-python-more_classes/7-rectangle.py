#!/usr/bin/python3
# 6-rectangle.py
"""representing the class"""

class Rectangle:
    """representing the rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the width of the retaingle"""
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
        """calculate the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)

    def __str__(self):
        """returns a printable representation of the rectangle"""
        self.__stri = ""
        for char in range(self.__height):
            for symb in range(self.__width):
                self.__stri += Rectangle.print_symbol
            self.__stri += "\n"
        return self.__stri
     
     
    def __repr__(self):
        """returns a string representation of rectangle"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """delete an instanc e of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
