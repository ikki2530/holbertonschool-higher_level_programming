#!/usr/bin/python3
"""from_json_string"""
import json


def from_json_string(my_str):
    """convert a json string to python obj

    Arguments:
        my_str {string} -- json string

    Returns:
        [object] -- python object
    """
    data = json.loads(my_str)
    return data
