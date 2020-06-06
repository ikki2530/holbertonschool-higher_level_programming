#!/usr/bin/python3
import unittest
from models.base import Base


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
