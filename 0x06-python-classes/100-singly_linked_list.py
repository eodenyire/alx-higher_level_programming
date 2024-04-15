#!/usr/bin/python3
""" Implementation of a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None) -> None:
        """Initializes the node with data and a reference to the next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data stored in the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the reference to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the reference to the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes an empty singly linked list"""
        self.head = None

    def __str__(self):
        """Returns a string representation of the singly linked list"""
        all_data = ""
        tmp = self.head
        while tmp:
            all_data += str(tmp.data) + "\n"
            tmp = tmp.next_node
        return all_data[:-1]

    def sorted_insert(self, value):
        """Inserts a new node with the given value into the sorted position in the list"""
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        if value < temp.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node

