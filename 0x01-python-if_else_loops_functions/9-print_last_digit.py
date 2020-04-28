#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        dig = number % 10
    else:
        number = number * (-1)
        dig = number % 10
    print("{0:d}".format(dig), end="")
    return dig
