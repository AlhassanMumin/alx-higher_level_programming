#!/usr/bin/python3
# rectangle.py
"""the definition of the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """the rectangle lass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the constructor
         Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """get the width of rectangle"""
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
        """Get the height of the rectangle"""
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
        """Get the x value"""
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
        """get the y value"""
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
        return self.width * self.height

    def display(self):
        """Display a rectangle with a '#'"""
        if self.height == 0 or self.width == 0:
            print("")
            return

        for bredth in range(self.height):
            for depth in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({})  {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """updates the instance attributes

        Args:
            *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents width attribute
            - 3rd argument represent height attribute
            - 4th argument represents x attribute
            - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if len(args) == 0:
            pass
        elif len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id, self.width = args
        elif len(args) == 3:
            self.id, self.width, self.height = args
        elif len(args) == 4:
            self.id, self.width, self.height, self.x = args
        else:
            self.id, self.width, self.height, self.x, self.y = args
