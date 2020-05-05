#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if my_list:
        if idx < 0:
            new = my_list[:]
        elif idx > (len(my_list) - 1):
            new = my_list[:]
        else:
            new = my_list[:]
            new[idx] = element
    return new
