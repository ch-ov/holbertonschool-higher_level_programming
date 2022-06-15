#!/usr/bin/python3
"""1. Base class"""


import json


class Base:
    """This class will be the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    """end 1. Base class"""

    """15. Dictionary to JSON string"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = "[]"
            return list_dictionaries
        return json.dumps(list_dictionaries)
    """end 15. Dictionary to JSON string"""

    """16. JSON string to file"""
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        json_string_repr = []
        if list_objs is not None:
            for objs in list_objs:
                json_string_repr.append(cls.to_dictionary(objs))
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as file:
            file.write(cls.to_json_string(json_string_repr))
    """end 16. JSON string to file"""

    """17. JSON string to dictionary"""
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            json_list_repr = []
            return json_list_repr
        return json.loads(json_string)
    """end 17. JSON string to dictionary"""

    """18. Dictionary to Instance"""
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy
    """end 18. Dictionary to Instance"""
