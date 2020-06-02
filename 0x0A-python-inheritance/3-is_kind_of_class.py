#!/usr/bin/python3
"""Function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Arguments:
        obj {any type} -- any type of object
        a_class {any type} -- any kind of class

    Returns:
        bool -- True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
