#!/usr/bin/python3
# square.py
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """get the width value"""
        return self.width

    @size.setter
    def size(self, square_side):
        """sets the width and height"""
        self.width = square_side
        self.height = square_side

    def __str__(self):
        """the magic str method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
