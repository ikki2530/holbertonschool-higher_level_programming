#!/usr/bin/python3
"""Base class tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test for base class
    Test for instances and its attributes and methods
    Args:
        unittest ([type]): python module for tests
    """

    def test_id_12(self):
        """testing initial id
        """
        b = Base()
        self.assertEqual(b.id, 1)
        b12 = Base(12)
        self.assertEqual(b12.id, 12)

    # def test_id_positive(self):
    #     """testing positive id
    #     """
    #     b1 = Base()
    #     self.assertEqual(b1.id, 2)
    #     b2 = Base()
    #     self.assertEqual(b2.id, 3)
    #     b3 = Base()
    #     self.assertEqual(b3.id, 4)  # id 4

    # def test_id_negative(self):
    #     """testing negative ids
    #     """
    #     b5 = Base(-5)
    #     self.assertEqual(b5.id, -5)

    # def test_id_float(self):
    #     """testing id floats
    #     """
    #     b6 = Base(6.0)
    #     self.assertEqual(b6.id, 6.0)

    # def test_id_string(self):
    #     """testing id strings
    #     """
    #     b7 = Base("Holberton")
    #     self.assertEqual(b7.id, "Holberton")

    # def test_id_bool(self):
    #     """testing bool ids
    #     """
    #     b8 = Base(True)
    #     self.assertEqual(b8.id, True)

    # def test_id_list(self):
    #     """testing list ids
    #     """
    #     b9 = Base([1])
    #     self.assertEqual(b9.id, [1])

    # def test_id_tuple(self):
    #     """testing tuple ids
    #     """
    #     b10 = Base((15, 16))
    #     self.assertEqual(b10.id, (15, 16))

    # def test_id_dict(self):
    #     """testing dict ids
    #     """
    #     b11 = Base({1, 2})
    #     self.assertEqual(b11.id, {1, 2})

    # test to json staticmethod
    def test_tojson(self):
        """testing to json method
        """
        b12 = Rectangle(10, 7, 2, 8)
        dictionary = b12.to_dictionary()
        strjson = Base.to_json_string([dictionary])
        self.assertTrue(type(dictionary) is dict)
        self.assertTrue(type(strjson) is str)
