#!/usr/bin/python3
def uppercase(str):
    j = 1
    for i in str:
        if i in "abcdefghijklmnopqrstuvwxyz":
            k = ord(i)
            l = k - 32
            str = str[0:j - 1] + chr(l) + str[j:]
        j = j + 1
    print("{:s}".format(str))
