#!/usr/bin/python
"""
provides a class, MyList
"""


class MyList(list):
    """
    inherits from list
    """

    def print_sorted(self):
        """
        prints the list, sorted in ascending order
        """
        print(sorted(self))
