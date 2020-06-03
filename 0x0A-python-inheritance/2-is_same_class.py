#!/usr/bin/python3
"""Function is_same_class"""


def is_same_class(obj, a_class):
    """checks if obj is a_class

    Arguments:
        obj {any type} -- object
        a_class {any type} -- class

    Returns:
        bool -- True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
