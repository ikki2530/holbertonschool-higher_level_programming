#!/usr/bin/python3
"""save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """save my_ob in a file

    Arguments:
        my_obj {any type} -- python object
        filename {string} -- file name

    Returns:
        [type] -- [description]
    """
    with open(filename, "w", encoding="utf-8") as f:
        data = json.dump(my_obj, f)
    return data
