#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("{0:s}".format("FizzBuzz"), end=" ")
        elif i % 3 == 0:
            print("{0:s}".format("Fizz"), end=" ")
        elif i % 5 == 0:
            print("{0:s}".format("Buzz"), end=" ")
        else:
            print("{0:d}".format(i), end=" ")
