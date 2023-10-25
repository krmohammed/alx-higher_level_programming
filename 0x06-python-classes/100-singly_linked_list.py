#!/usr/bin/python3
"""
Implementation of linked list in python
"""


class Node:
    """
    a node class to represent a linked list node
    """
    def __init__(self, data, next_node=None):
        """
        initializes private attributes

        Args:
            data (int): node data
            next_node (Node): next node element
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data attribute's getter function

        Returns:
            data attribute's value
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node attribute's getter function

        Returns:
            next_node attribute's value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (isinstance(value, Node) or value == None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    linked in class to implement a linked list
    """
    def __init__(self):
        """
        initializes the head node

        Args:
            head (Node): head node
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new node into the correct sorted position

        Args:
            value (int): value for node data
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            ptr = self.__head
            while ptr.next_node is not None and ptr.next_node.data < value:
                ptr = ptr.next_node
            new_node.next_node = ptr.next_node
            ptr.next_node = new_node

    def __str__(self):
        my_list = ''
        ptr = self.__head
        while ptr is not None:
            my_list += str(ptr.data) + '\n'
            ptr = ptr.next_node
        return my_list.rstrip()
