#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass."""
        self.__radiuc = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
