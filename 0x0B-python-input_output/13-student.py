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

    def to_json(self, attrs=None):
        """ to dict with all attributes

        Keyword Arguments:
            attrs {list} -- list of keys (default: {None})

        Returns:
            dict -- dictionary with respect keys of attrs
        """
        new = {}
        if type(attrs) != list:
            return self.__dict__
        for i in attrs:
            if type(i) != str:
                return self.__dict__

        for k, v in self.__dict__.items():
            for key in attrs:
                if key == k:
                    new[k] = v
        return new

    def reload_from_json(self, json):
        """reload from a dict

        Arguments:
            json {dict} -- disctionary with the values to be replaced
        """
        for k, v in json.items():
            setattr(self, k, v)
