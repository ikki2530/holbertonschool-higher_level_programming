#!/usr/bin/python3
"""indentation function"""


def text_indentation(text):
    """Print a text

    Arguments:
        text {string} -- text to be printed

    Raises:
        TypeError: text must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    new = text
    new = new.replace('. ', '.\n\n')
    new = new.replace(': ', ':\n\n')
    new = new.replace('? ', '?\n\n')
    print("{}".format(new), end="")
