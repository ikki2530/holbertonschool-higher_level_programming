#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    if list_of_integers:
        lg = len(list_of_integers)
        if lg == 1:
            return list_of_integers[0]
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[lg - 1] >= list_of_integers[lg - 2]:
            return list_of_integers[lg - 1]
        for i in range(1, lg - 1):
            num = list_of_integers[i]
            if num > list_of_integers[i - 1] and num > list_of_integers[i + 1]:
                return num
    return None
