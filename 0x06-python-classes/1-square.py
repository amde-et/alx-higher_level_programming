#!/usr/bin/python3
""" Creates an empty class called Square
"""


class Square:
    """ Empty class with size private attribute
    """
    def __init__(self, size):
        """
                Instantiation with size
        Args:
            size: size of the square
        """
        self.__size = size
