#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        delkeys = []
        for key, val in a_dictionary.items():
            if val == value:
                delkeys.append(key)
        for key2 in delkeys:
            del a_dictionary[key2]
    return a_dictionary
