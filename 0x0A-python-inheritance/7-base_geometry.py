#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class for geometry
    """

    def area(self):
        """calculates the area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer

        Arguments:
            name {string} -- name
            value {int} -- value

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
