#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    """defines a student by: (based on 10-student.py)"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """retrieves a dictionary representation of a Student instance \
    (same as 8-class_to_json.py)"""
    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            new_dict = {}
            for element in attrs:
                if element in self.__dict__:
                    new_dict[element] = self.__dict__[element]
            return new_dict
        return self.__dict__
    """replaces all attributes of the Student instance"""
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
