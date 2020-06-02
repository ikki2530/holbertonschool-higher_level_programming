#!/usr/bin/python3
"""Class that inherits form list"""


class MyList(list):
    """Class that inherits form list

    Arguments:
        list {list} -- list inheritance
    """

    def print_sorted(self):
        """Method for print a list sroted
        """
        new = sorted(self)
        print(new)
