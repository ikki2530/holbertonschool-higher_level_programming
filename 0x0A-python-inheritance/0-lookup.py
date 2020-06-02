#!/usr/bin/python3
"""function lookup"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Arguments:
        obj {any type} -- Can be an object of any type

    Returns:
        list -- list of available attributes and methods of an object
    """
    new = dir(obj)
    return new
