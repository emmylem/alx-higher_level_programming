#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Contains a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square."""
        self.size = size

    @property
    def size(self):
        """Getting the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (not type(value) is int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
