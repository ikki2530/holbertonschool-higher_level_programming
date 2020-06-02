#!/usr/bin/python3
"""Class that inherits form list"""


class MyList(list):
    """Class that inherits form list

    Arguments:
        list {list} -- list inheritance
    """

    def __init__(self):
        """Initialize the list
        """
        list.__init__(self)

    def print_sorted(self):
        """Method for print a list sroted
        """
        new = sorted(self)
        print(new)
        # num = -1000
        # temp = 0
        # new = self[:]
        # for i in range(len(new)):
        #     print(num)
        #     if new[i] < num:
        #         temp = num
        #         new[i - 1] = new[i]
        #         new[i] = temp
        #     num = new[i]
        # print(new)
