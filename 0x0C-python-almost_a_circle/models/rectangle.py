#!/usr/bin/python3
# rectangle.py
"""the definition of the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """the rectangle lass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """setter mehto"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format('width'))
        if value <= 0:
            raise ValueError("{} must be > 0".format('width'))
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """get and set method for height"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format('height'))
        if value <= 0:
            raise ValueError("{} must be > 0".format('height'))
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """get/set methods for x"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format('x'))
        if value < 0:
            raise ValueError("{} must be > 0".format('x'))
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """get/set methond"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format('y'))
        if value < 0:
            raise ValueError("{} must be > 0".format('y'))
        self.__y = value

    def area(self):
        """computes the area of the triangle"""
        return self.__width*self.__height

    def display(self):
        """Display a rectangle with a '#'"""
        for bredth in range(self.__height):
            for depth in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({})  {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """updates the instance attributes"""
        if len(args) == 0:
            pass
        elif len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id, self.__width = args
        elif len(args) == 3:
            self.id, self.__width, self.__height = args
        elif len(args) == 4:
            self.id, self.__width, self.__height, self.__x = args
        else:
            self.id, self.__width, self.__height, self.__x, self.__y = args
