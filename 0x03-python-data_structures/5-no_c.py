#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        my_list = list(my_string)
        my_string = ""
        for i in my_list:
            if i not in "cC":
                my_string += i
    return my_string
