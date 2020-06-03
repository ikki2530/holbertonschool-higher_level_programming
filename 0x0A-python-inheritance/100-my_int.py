#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """[summary]

    Arguments:
        int {class} -- class int
    """

    def __ne__(self, other):
        """!=

        Arguments:
            other {int} -- integer

        Returns:
            bool -- True
        """
        return True

    def __eq__(self, other):
        """==

        Arguments:
            other {int} -- integer

        Returns:
            other -- False
        """
        return False
