#!/usr/bin/python3
def weight_average(my_list=[]):
    sumn = 0
    div = 0
    if my_list:
        for (i, j) in my_list:
            sumn += i * j
            div += j
        if div != 0:
            total = sumn / div
        return total
    return sumn
