#!/usr/bin/python3
def max_integer(my_list=[]):
    manum = 0
    if my_list:
        for num in my_list:
            if manum < num:
                manum = num
    else:
        return None
    return manum
