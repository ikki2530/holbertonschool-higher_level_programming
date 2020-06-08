#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_12(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b12 = Base(12)
        self.assertEqual(b12.id, 12)

    def test_id_positive(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)  # id 4

    def test_id_negative(self):
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)

    def test_id_float(self):
        b6 = Base(6.0)
        self.assertEqual(b6.id, 6.0)

    def test_id_string(self):
        b7 = Base("Holberton")
        self.assertEqual(b7.id, "Holberton")

    def test_id_bool(self):
        b8 = Base(True)
        self.assertEqual(b8.id, True)

    def test_id_list(self):
        b9 = Base([1])
        self.assertEqual(b9.id, [1])

    def test_id_tuple(self):
        b10 = Base((15, 16))
        self.assertEqual(b10.id, (15, 16))

    def test_id_dict(self):
        b11 = Base({1, 2})
        self.assertEqual(b11.id, {1, 2})

    # test to json staticmethod
    def test_tojson(self):
        b12 = Rectangle(10, 7, 2, 8)
        dictionary = b12.to_dictionary()
        strjson = Base.to_json_string([dictionary])
        self.assertTrue(type(dictionary) is dict)
        self.assertTrue(type(strjson) is str)

    def test_savetofile(self):
        b13 = Rectangle(10, 7, 2, 8, 400)
        b14 = Rectangle(5, 4, 3, 2, 401)
        Rectangle.save_to_file([b13, b14])
        with open("Rectangle.json", "r") as file:
            num = file.read()
        lista = list(num)
        self.assertTrue(lista == [{"y": 8, "x": 2, "width": 10, "id": 400, "height": 7}, {
                        "y": 2, "x": 3, "width": 5, "id": 401, "height": 4}])
        print(type(num))
