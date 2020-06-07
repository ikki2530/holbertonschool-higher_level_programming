#!/usr/bin/python3
from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
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

