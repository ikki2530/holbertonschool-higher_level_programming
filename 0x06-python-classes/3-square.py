#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """__init__  method
        Args:
            param1 (size): side of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """"area of a square
        Returns:
        the area of the square of size
        """
        return self.__size * self.__size
