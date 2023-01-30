#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a  Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self._width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get/set the width of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
