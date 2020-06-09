#!/usr/bin/python3
"""class Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square

    Args:
        Rectangle (obj): square inherits form Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class

        Args:
            size (int): size of the square sides
            x (int, optional): horizontal spaces(coordinates). Defaults to 0.
            y (int, optional): Vertical spaces(coordinate). Defaults to 0.
            id ([type], optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size

        Returns:
            int: size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter method

        Args:
            value (int): new value for size

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """

        self.width = value
        self.height = value

    def __str__(self):
        """string format to print

        Returns:
            [str]: string with information about the square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update method for square
        """
        sqrlist = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(sqrlist)):
                if i < len(args):
                    # call to setter method
                    setattr(self, sqrlist[i], args[i])
        else:
            if kwargs and len(kwargs) != 0:
                for k in sqrlist:
                    for key, value in kwargs.items():
                        if k == key:
                            setattr(self, key, value)

    def to_dictionary(self):
        """convert to dictionary

        Returns:
            dict: convert an instance to dictionaty
        """
        new = {}
        data = ["id", "size", "x", "y"]
        for i in range(len(data)):
            new[data[i]] = getattr(self, data[i])
        return new
