#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    ac = len(argv)
    if ac != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    else:
        op = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if op == "+":
            print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
        elif op == "-":
            print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
