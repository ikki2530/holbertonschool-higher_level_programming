#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """[summary]

    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
