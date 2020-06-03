#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """append content to the file

    Keyword Arguments:
        filename {str} -- file name (default: {""})
        text {str} -- text to be appended (default: {""})

    Returns:
        int -- number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        num = f.write(text)
    return num
