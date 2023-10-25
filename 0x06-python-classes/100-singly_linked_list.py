#!/usr/bin/python3
class Node:
    """
    """
    def __init__(self, data, next_node=None):
        """
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
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
    """
    def __init__(self):
        """
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        """
        if self.__head == None:
            self.__head = Node(value)
            return
        ptr = Node(value)
        tmp = self.__head
        tmp2 = tmp.next_node
        while tmp is not None:
            if value <= tmp.data:
                break
            tmp = tmp.next_node
        ptr.next_node = tmp.next_node
        tmp.next_node = ptr
