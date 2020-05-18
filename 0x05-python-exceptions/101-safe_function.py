#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        val = fct(*args)
    except ArithmeticError as ar:
        print("Exception: {}".format(ar), file=sys.stderr)
        val = None
    except LookupError as ar:
        print("Exception: {}".format(ar), file=sys.stderr)
        val = None
    return val
