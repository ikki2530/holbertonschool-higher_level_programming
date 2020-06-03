#!/usr/bin/python3
"""class_to_json function"""


def class_to_json(obj):
    """class to json

    Arguments:
        obj {instance} -- instance

    Returns:
        dict -- dictionary with info about the object
    """
    return obj.__dict__
