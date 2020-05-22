#!/usr/bin/python3
"""Function to printdasd a name"""


def say_my_name(first_name, last_name=""):
    """Print my name and last name

    Arguments:
        first_name {str} -- First name

    Keyword Arguments:
        last_name {str} -- last name (default: {""})

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    if first_name == "" and last_name == "":
        print("My name is {:s} {:s}".format(first_name, last_name))
    if first_name:
        print("My name is {:s} {:s}".format(first_name, last_name))
