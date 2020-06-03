#!/usr/bin/python3
"""number_of_lines function"""


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
