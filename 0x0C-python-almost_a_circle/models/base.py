#!/usr/bin/python3
"""
"""
import json
from os.path import exists


class Base:
    """
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as file:
            json_list = []
            if list_objs is None:
                file.write(f"{json_list}")
            else:
                for obj in list_objs:
                    json_list.append(obj.to_dictionary())
                b = cls.to_json_string(json_list)
                file.write(b)

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
        """
        dummy = cls(4, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        """
        filename = f"{cls.__name__}.json"
        if not exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as file:
            json_data = file.read()
            json_itr = cls.from_json_string(json_data)
        return [cls.create(**item) for item in json_itr]
