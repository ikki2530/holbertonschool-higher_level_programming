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
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates the area of the square

        Returns:
            int -- area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """returns the string

        Returns:
            string -- A messagge
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
