#!/usr/bin/python3
"""Base class"""
import json
import os.path


class Base:
    """Base class for the Almost circle project

    Returns:
        [type]: [description]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for Base class

        Args:
            id (int, optional): id of the figure. Defaults to None.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries and list_dictionaries == None:
            stringjson = "[]"
        else:
            stringjson = json.dumps(list_dictionaries)
        return stringjson

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        new = []
        if list_objs is None:
            jsonstring = cls.to_json_string(new)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(jsonstring)
        else:
            for i in list_objs:
                if isinstance(i, cls):
                    new.append(i.to_dictionary())
            jsonstring = cls.to_json_string(new)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(jsonstring)

    @staticmethod
    def from_json_string(json_string):
        new = []
        if not json_string or json_string is None:
            return []
        else:
            # from json string to python dict
            data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            r = cls(1, 1)
            r.update(**dictionary)
        elif cls.__name__ == "Square":
            r = cls(5)
            r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            list_out = []
            with open(filename, "r", encoding="utf-8") as f:
                data_fromfile = f.read()
            print(data_fromfile)
            # from json string to python
            list_dict = cls.from_json_string(data_fromfile)
            for dic in list_dict:
                r = cls.create(**dic)
                list_out.append(r)
            return list_out
        else:
            return []
