#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        for k in sorted(list(a_dictionary.keys())):
            if k == key:
                del a_dictionary[key]
    return a_dictionary
