#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def __init__(self, size=0, position=(0,0)):
        """__init__  method
        Args:
            param1 (size): side of the square.
            param2 (position): a tuple with coordinates fo spaces
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """"area of a square
        Returns:
        the area of the square of size
        """
        return self.__size * self.__size

    def my_print(self):
        """"my_print: prints square
        Returns:
        Nothing
        """
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" "*self.__position[0], end="")
            print("#"*self.__size)