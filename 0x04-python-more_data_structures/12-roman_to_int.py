#!/usr/bin/python3
def roman_to_int(roman_string):
    r_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    minn = 0
    if roman_string and (roman_string is not None) and type(roman_string) == str:
        for rom in roman_string:
            if rom not in "IVXLCDM":
                return 0
            for k, val in r_nums.items():
                if k == rom:
                    if minn < val:
                        num = num - (minn * 2)
                    num += val
                    minn = val
        return num
    return 0
