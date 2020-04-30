#!/usr/bin/python3
import sys

if __name__ == "__main__":
    ac = len(sys.argv)
    for i in range(ac):
        if ac == 1:
            print("{0:d} arguments.".format(i))
        else:
            if i == 0:
                if ac == 2:
                    print("{0:d} argument:".format(ac - 1))
                else:
                    print("{0:d} arguments:".format(ac - 1))
            else:
                print("{0:d}: {1:s}".format(i, sys.argv[i]))
