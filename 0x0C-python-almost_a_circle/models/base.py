#!/usr/bin/python3
"""
Provides Base class, parent class for
`Rectangle and `Square
"""
import json
from os.path import exists


class Base:
    """
    Parent class for `Rectangle and `Square
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes Base class
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        serializes `list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            JSON representation of `list_dictionaries
        """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON representation of `list_objs
        to a file

        Args:
            list_objs (list): list of instances
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as file:
            json_list = []
            if list_objs is None:
                file.write(f"{json_list}")
            else:
                for obj in list_objs:
                    json_list.append(obj.to_dictionary())
                json_string = cls.to_json_string(json_list)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        deserializes `json_string

        Args:
            json_string (str): JSON string

        Returns:
            list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates new instance from details in
        `dictionary

        Args:
            dictionary (dict/kwargs): dictionary

        Returns:
            an instances with attributes set
        """
        dummy = cls(4, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        creates new instances

        Returns:
            a list of instances
        """
        filename = f"{cls.__name__}.json"
        if not exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as file:
            json_data = file.read()
            json_itr = cls.from_json_string(json_data)
        return [cls.create(**item) for item in json_itr]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes `list_objs

        Args:
            list_objs (list): list of objects
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                json_list = []
            else:
                json_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(json_list)
            file.write(json_string)

    @classmethod
    def load_from_file_csv(cls):
        """
        create new instances

        Returns:
            list of instances
        """
        filename = f"{cls.__name__}.csv"

        if not exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as file:
            json_data = cls.from_json_string(file.read())
        return [cls.create(**data) for data in json_data]
