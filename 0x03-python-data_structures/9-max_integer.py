#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        manum = my_list[0]
        for num in my_list:
            if manum < num:
                manum = num
    else:
        return None
    return manum
