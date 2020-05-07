#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newx2 = {}
    if a_dictionary:
        for key in sorted(a_dictionary.keys()):
            newx2[key] = a_dictionary[key] * 2
    return newx2
