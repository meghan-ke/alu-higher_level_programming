#!/usr/bin/python3
"""Module that defines a Square class."""

class Square:
    """Class that defines a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """Initializes a new square instance.

        Args:
            size (int): The size of the square (no type/value checks for now).
        """
        self.__size = size
