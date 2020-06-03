#!/usr/bin/python3
"""load_from_json_file function"""
import json


def load_from_json_file(filename):
    """load from json file

    Arguments:
        filename {str} -- file name

    Returns:
        python object -- python object
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
