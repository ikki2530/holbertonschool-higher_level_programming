#!/usr/bin/python3
"""Base class"""
import json
import csv
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
            id (int, optional): id of the . Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert a python obj to json string

        Args:
            list_dictionaries (list of dictionaries): list with
            any kind of information

        Returns:
            string: json string
        """
        if not list_dictionaries and list_dictionaries is None:
            stringjson = "[]"
        else:
            stringjson = json.dumps(list_dictionaries)
        return stringjson

    @classmethod
    def save_to_file(cls, list_objs):
        """save into a file

        Args:
            list_objs (list): list of python objects
        """
        filename = cls.__name__ + ".json"
        new = []
        if list_objs is None:
            jsonstring = cls.to_json_string(new)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(jsonstring)
        else:
            for i in list_objs:
                new.append(i.to_dictionary())
            jsonstring = cls.to_json_string(new)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(jsonstring)

    @staticmethod
    def from_json_string(json_string):
        """from json string to python

        Args:
            json_string (json string): json string to be
            converted to python object

        Returns:
            [type]: [description]
        """
        new = []
        if not json_string or json_string is None:
            return []
        else:
            # from json string to python dict
            data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """Create instance to cls class

        Returns:
            cls: cls instance
        """
        if cls.__name__ == "Rectangle":
            r = cls(1, 1)
            r.update(**dictionary)
        elif cls.__name__ == "Square":
            r = cls(5)
            r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """load from json file

        Returns:
            python object: load json
            and convert data to python
        """
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            list_out = []
            with open(filename, "r", encoding="utf-8") as f:
                data_fromfile = f.read()
            # from json string to python
            list_dict = cls.from_json_string(data_fromfile)
            for dic in list_dict:
                r = cls.create(**dic)
                list_out.append(r)
            return list_out
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save data to csv file

        Args:
            list_objs (Rectangle, Square): list of instances from
            Rectangle and Square
        """
        filename = cls.__name__ + ".csv"
        new = []
        for obj in list_objs:
            new.append(obj.to_dictionary())
        with open(filename, "w") as f:
            csv_write = csv.writer(f)
            i = 0
            for dic in new:
                if i == 0:
                    header = dic.keys()
                    h = list(header)
                    csv_write.writerow(h)
                    i += 1
                val = list(dic.values())
                csv_write.writerow(val)

    @classmethod
    def create_csv(cls, **dictionary):
        """create a csv file

        Returns:
            cls instance: dummy created isntance
        """
        if cls.__name__ == "Rectangle":
            r = cls(1, 1)
            r.update(**dictionary)
        elif cls.__name__ == "Square":
            r = cls(5)
            r.update(**dictionary)
        return r

    @classmethod
    def load_from_file_csv(cls):
        """load information from csv file

        Returns:
            list: list of instances of cls
        """
        filename = cls.__name__ + ".csv"
        new_dict = {}
        new_list = []
        if os.path.isfile(filename) is False:
            return []
        else:
            new = []
            with open(filename, mode="r", encoding="utf-8") as f:
                reader = csv.reader(f)
                # header
                header = next(reader)
                # lists and dictionary
                new_dict = {}  # diccionario
                new_list = []  # lista de diccionarios
                list_out = []  # lista de retorno
                i = 0
                for row in reader:
                    i = 0
                    # val is the corresponding value to the key
                    for val in row:
                        new_dict[header[i]] = int(val)
                        i += 1
                    new_list.append(new_dict)
                    new_dict = {}
                # createing instances with the data
                for dic in new_list:
                    r = cls.create_csv(**dic)
                    list_out.append(r)
            return list_out
