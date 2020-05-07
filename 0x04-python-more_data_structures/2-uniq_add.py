#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    result = 0
    if my_list:
        new = list(set(my_list))
        for num in new:
            result += num
    return result
