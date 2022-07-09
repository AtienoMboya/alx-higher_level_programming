#!/usr/bin/python3
"""Rectangle class inherits from Base class."""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class Rectangle.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
