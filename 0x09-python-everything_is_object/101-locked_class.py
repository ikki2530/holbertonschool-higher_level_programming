#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """LockedClass
    """
    __slots__ = "first_name"

    def __init__(self, first_name=""):
        """__initi__

        Arguments:
            first_name {string} -- first name
        """
        self.first_name = first_name
