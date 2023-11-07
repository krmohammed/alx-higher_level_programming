#!/usr/bin/python3
"""
provides MyInt class
"""


class MyInt(int):
    """class inherits from int
    """
    def __eq__(self, other):
        """
        Inverts == to !=
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts != to ==
        """
        return super().__eq__(other)
