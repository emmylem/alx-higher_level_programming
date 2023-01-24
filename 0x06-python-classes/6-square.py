#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Contains a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square."""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Getting the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size."""
        if (not type(value) is int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getting the size."""
        return (self.position)

    @position.setter
    def position(self, value):
        if (not type(value) is tuple
            or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
