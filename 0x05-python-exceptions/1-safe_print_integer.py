#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val = isinstance(value, int)
        if val:
            print("{:d}".format(value))
            return True
        raise ValueError
    except ValueError:
        return False
