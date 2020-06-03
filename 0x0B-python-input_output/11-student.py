#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student
    """

    def __init__(self, first_name, last_name, age):
        """initialize the class

        Arguments:
            first_name {str} -- first name
            last_name {str} -- last name
            age {int} -- age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """convert to dict

        Returns:
            dict -- information about the object
        """
        return self.__dict__
