#!/usr/bin/python3
for dec in range(0, 9):
    for un in range(dec + 1, 10):
        if dec == 8 and un == 9:
            print("{0:d}{1:d}".format(dec, un))
        else:
            print("{0:d}{1:d}".format(dec, un), end=", ")
