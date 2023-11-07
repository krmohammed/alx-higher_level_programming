#!/usr/bin/python3
"""
provides the class Student
"""


class Student:
    """
    """
    def __init__(self, first_name, last_name, age):
        """initializes instance variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation
            of `self
        """
        if attrs is not None:
            return {i: self.__dict__[i] for i in attrs if i in self.__dict__}
        return self.__dict__
