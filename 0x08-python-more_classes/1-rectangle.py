#!/usr/bin/python3


"""Defines a class Rectangle."""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

    def width(self, value):
        """sets the width value.

        Args:
            value: the value to be set
        """
        self.__width = value

        if (self.__width.isinstance()) is False:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")

    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    def height(self, value):
        """Sets the value of the height.

        Args:
            value: the value to be set
        """
        self.__height = value
        if (self.__height.isinstance()) is False:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")

    def height(self):
        """Retrieves the height."""
        return self.__height
