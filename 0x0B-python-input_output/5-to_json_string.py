#!/usr/bin/python3
"""to_json_string function"""
import json


def to_json_string(my_obj):
    """convert to json

    Arguments:
        my_obj {any type} -- object to be converted

    Returns:
        string -- json string
    """
    data = json.dumps(my_obj)
    return data
