#!/usr/bin/python3
"""Module that defines a Rectangle class with all core behaviors."""


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, return 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return a string that recreates the rectangle using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        print("Bye rectangle...")

