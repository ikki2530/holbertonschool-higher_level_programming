#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ac = len(sys.argv)
    sum = 0
    for i in range(ac):
        if i > 0:
            num = int(sys.argv[i])
            sum += num
    print("{0:d}".format(sum))
