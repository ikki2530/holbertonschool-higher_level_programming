#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    ac = len(sys.argv)
    if ac != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)
    else:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op == "+":
            print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
        elif op == "-":
            print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
        else:
            print("{}".format("Unknown operator. Available operators:"), end="")
            print("{}".format(" +, -, * and /"))
            sys.exit(1)
