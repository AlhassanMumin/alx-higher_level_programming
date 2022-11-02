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

    def update(self, *args, **kwargs):
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
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'size':
                    self.size = value
                if key == 'id':
                    self.id = value
        elif len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id, self.size = args
        elif len(args) == 3:
            self.id, self.size, self.x = args
        elif len(args) == 4:
            self.id, self.size, self.x, self.y = args
        else:
            pass

    def to_dictionary(self):
        """Dictionary representation of square"""
        return{
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
