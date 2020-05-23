#!/usr/bin/python3
""" print a square #"""


def print_square(size):
    """prints a square of #

    Arguments:
        size {int} -- size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) != float and size < 0:
        TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        print("#" * size)
