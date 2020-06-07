#!/usr/bin/python3
"""square tests"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    # str for square
    def test_squarestr(self):
        s101 = Square(5, 3, 2, 101)
        self.assertEqual(s101.__str__(), "[Square] (101) 3/2 - 5")
        s102 = Square(5, 0, 0)
        self.assertEqual(s102.__str__(), "[Square] (14) 0/0 - 5")  # id 14
