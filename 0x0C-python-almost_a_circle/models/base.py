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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
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
                dict_list = [o.to_dictionary() for o in list_objs]
                jf.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """the json or dict representation"""
        if json_string is None:
            return "[]"
        if isinstance(json_string, dict):
            return json.dumps(json_string)
        return json.loads(json_string)
