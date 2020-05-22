#!/usr/bin/python3
"""Function to add two integers"""


def add_integer(a, b=98):
    """Add two integers

    Arguments:
        a {int} -- number to be added

    Keyword Arguments:
        b {int} -- Integer to be added (default: {98})

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        type -- returns the sum of a + b
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
