#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class for the Almost circle project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for Base class

        Args:
            id (int, optional): id of the figure. Defaults to None.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
