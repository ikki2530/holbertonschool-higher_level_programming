#!/usr/bin/python3
"""function add_attribute"""


def add_attribute(obj, name, val):
    """add an attribute

    Arguments:
        name {any type} -- name of the new attribute
        val {any type} -- value of the new attribute

    Raises:
        TypeError: can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = val
