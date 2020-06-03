#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """write a text in a file

    Keyword Arguments:
        filename {str} -- file name (default: {""})
        text {str} -- text to be write in the file (default: {""})

    Returns:
        int -- numbers of characters writted
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        num = f.write(text)
    return num
