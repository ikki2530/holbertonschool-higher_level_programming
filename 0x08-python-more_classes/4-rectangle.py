#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """__init__ initialize the objects

        Arguments:
            width {int} -- width of the rectangle
            height {int} -- height of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get the width

        Returns:
            int -- Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectangle

        Arguments:
            value {int} -- new value of the width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height

        Returns:
            int -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle

        Arguments:
            value {int} -- new value of the height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle

        Returns:
            [int] -- the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter

        Returns:
            int -- perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """use to fill a rectangle

        Returns:
            string -- square of #
        """
        rectang = ""
        if self.width == 0 or self.height == 0:
            return rectang
        else:
            for i in range(self.height):
                rectang += "#" * self.__width
                if i != (self.height - 1):
                    rectang += "\n"
            return rectang

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
