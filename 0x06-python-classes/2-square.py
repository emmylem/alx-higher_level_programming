#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Contains a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square."""
        if (not type(size) is int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
