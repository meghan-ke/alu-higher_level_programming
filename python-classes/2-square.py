#!/usr/bin/python3
"""Module that defines a Square class with size validation."""
  

class Square:
    """Class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
