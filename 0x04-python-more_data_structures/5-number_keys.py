#!/usr/bin/python3
def number_keys(a_dictionary):
    numb_keys = 0
    if a_dictionary:
        numb_keys = len(list(a_dictionary.keys()))
    return numb_keys
