#!/usr/bin/python3
# base.py
"""Definition of the class base"""
import json
from io import StringIO


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
            __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionary to json string
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file a json representation
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                [print("{}".format(o.to_dictionary())) for o in list_objs]
                dict_list = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(dict_list))
