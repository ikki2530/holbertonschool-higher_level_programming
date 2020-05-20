#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__  method
        Args:
            param1 (size): side of the square.
            param2 (position): a tuple with coordinates fo spaces
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Get/set the size property"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the size property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Get/set the size property"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """"area of a square
        Returns:
        the area of the square of size
        """
        return self.__size * self.__size

    def my_print(self):
        """"my_print
        Returns:
        Nothing
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" "*self.__position[0], end="")
            for j in range(self.size):
                print("#", end="")
            if i == (self.size - 1):
                print("", end="")
            else:
                print("")

    def __str__(self):
        if self.__size == 0:
            print("")
            return ""
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            if i == (self.__size - 1):
                print(" "*self.__position[0], end="")
                print("#"*self.__size, end="")
            else:
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
        return ""
