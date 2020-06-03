#!/usr/bin/python3
"""read_lines"""


def read_lines(filename="", nb_lines=0):
    """read nb_lines form the file

    Keyword Arguments:
        filename {str} -- file name (default: {""})
        nb_lines {int} -- numbr of lines (default: {0})
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines >= number_of_lines(filename):
            data = f.read()
            print(data, end="")
        else:
            for i in range(nb_lines):
                data = f.readline()
                print(data, end="")


def number_of_lines(filename=""):
    """counts the number of lines

    Keyword Arguments:
        filename {str} -- name of the file (default: {""})

    Returns:
        [int] -- number of lines
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lineNum = 1

        while True:
            # line has the content of each line
            line = f.readline()
            if not line:
                break
            lineNum += 1
        return lineNum - 1
