#!/usr/bin/python3
from .base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base

    Args:
        Base (class): Base class for the project
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
