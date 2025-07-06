#!/usr/bin/python3
"""
This module defines a Square class with size attribute validation and an area method.
"""

class Square:
    """Class that defines a square by size with validation and area calculation."""

    def __init__(self, size=0):
        self.size = size  # Will call the setter for validation

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
