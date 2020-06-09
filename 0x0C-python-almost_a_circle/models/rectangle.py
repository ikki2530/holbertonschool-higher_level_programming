#!/usr/bin/python3
"""Rectangle class"""
from .base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base

    Args:
        Base (class): Base class for the project
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x value. Defaults to 0.
            y (int, optional): y value. Defaults to 0.
            id (int, optional): id of the figure. Defaults to None.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get the width
        Returns:
            int -- Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter width method

        Args:
            value (int): new value

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get method for height

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter height method

        Args:
            value (int): new value

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x get method

        Returns:
            int: value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method

        Args:
            value (int): new value

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y get method

        Returns:
            int: y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method

        Args:
            value int: new value

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of the rectangle

        Returns:
            int: Rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """Display the rectangle
        """
        for j in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width)

    def __str__(self):
        """return a string with information about the instance

        Returns:
            str: information about rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updating the Rectangle values
        """
        new_list = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(new_list)):
                if i < len(args):
                    setattr(self, new_list[i], args[i])
        else:
            if kwargs and len(kwargs) != 0:
                for k in new_list:
                    for key, value in kwargs.items():
                        if k == key:
                            setattr(self, key, value)

    def to_dictionary(self):
        """convert to dictionary

        Returns:
            [dict]: dictionary with tje information for the instance
        """
        new = {}
        data = ["id", "width", "height", "x", "y"]
        for i in range(len(data)):
            new[data[i]] = getattr(self, data[i])
        return new
