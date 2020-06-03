#!/usr/bin/python3
"""function add_attribute"""


def add_attribute(cls, name, val):
    """add an attribute

    Arguments:
        name {any type} -- name of the new attribute
        val {any type} -- value of the new attribute

    Raises:
        TypeError: can't add new attribute
    """
    try:
        cls.name = val
    except:
        raise TypeError("can't add new attribute")
