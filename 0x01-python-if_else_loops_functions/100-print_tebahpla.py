#!/usr/bin/python3
lower = 0
for i in range(122, 96, -1):
    if lower % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i - 32)), end="")
    lower = lower + 1
