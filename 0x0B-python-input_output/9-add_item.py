#!/usr/bin/python3
""" main for the function"""
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """main for the program
    """
    filename = "add_item.json"
    if os.path.isfile(filename):
        my_obj = load_from_json_file(filename)
        my_obj += sys.argv[1:]
        save_to_json_file(list(my_obj), filename)
    else:
        save_to_json_file(list(sys.argv[1:]), filename)
