#!/usr/bin/python3
"""
Provides Base class, parent class for
`Rectangle and `Square
"""
import json
from os.path import exists
import csv
import turtle


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
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
        dummy = cls(1, 1)
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
            csv_data = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    csv_data.writerow([obj.id, obj.width, obj.height,
                                       obj.x, obj.y])
                if cls.__name__ == 'Square':
                    csv_data.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        create new instances

        Returns:
            list of instances
        """
        filename = f"{cls.__name__}.csv"
        list_data = []

        with open(filename, "r", encoding='utf-8', newline='') as file:
            csv_data = csv.reader(file)
            for row in csv_data:
                if len(row) == 0:
                    continue
                if cls.__name__ == 'Rectangle':
                    data = cls.create(id=int(row[0]), width=int(row[1]),
                                      height=int(row[2]), x=int(row[3]),
                                      y=int(row[4]))
                elif cls.__name__ == 'Square':
                    data = cls.create(id=int(row[0]), size=int(row[1]),
                                      x=int(row[2]), y=int(row[3]))
                list_data.append(data)
        return list_data

    @staticmethod
    def draw(list_rectangles, list_squares):
        turt = turtle.Turtle()
        turt.screen.bgcolor('#2A4494')
        turt.color('#44CFCB', '#5299D3')
        turt.speed('slowest')
        turt.pensize(3)

        for rt in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rt.width, rt.height)
            turt.down()
            turt.begin_fill()

            for i in range(2):
                turt.forward(rt.width)
                turt.left(90)
                turt.forward(rt.height)
                turt.left(90)
            turt.end_fill()
            turt.hideturtle()

        for sqr in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.size, sqr.size)
            turt.down()
            turt.begin_fill()

            for i in range(2):
                turt.forward(sqr.size)
                turt.left(90)
                turt.forward(sqr.size)
                turt.left(90)
            turt.end_fill()
            turt.hideturtle()

        turtle.exitonclick()
