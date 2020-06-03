#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class

    Arguments:
        Rectangle {Class} -- inheritance
    """

    def __init__(self, size):
        """initialize the instances

        Arguments:
            size int -- size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
