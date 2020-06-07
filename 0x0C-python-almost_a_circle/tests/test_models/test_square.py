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

    # update tests
    def test_squareupdate(self):
        s103 = Square(5)
        self.assertEqual(s103.__str__(), "[Square] (15) 0/0 - 5")  # id 15
        s103.update(103)
        self.assertEqual(s103.__str__(), "[Square] (103) 0/0 - 5")
        s103.update(103, 2)
        self.assertEqual(s103.__str__(), "[Square] (103) 0/0 - 2")
        s103.update(103, 2, 3)
        self.assertEqual(s103.__str__(), "[Square] (103) 3/0 - 2")
        s103.update(103, 2, 3, 4)
        self.assertEqual(s103.__str__(), "[Square] (103) 3/4 - 2")
        s103.update(y=1)
        self.assertEqual(s103.__str__(), "[Square] (103) 3/1 - 2")
        s103.update(size=7, id=4000, y=1)
        self.assertEqual(s103.__str__(), "[Square] (4000) 3/1 - 7")

    def test_errorsupdate(self):
        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(x=-3, size="hola")

        with self.assertRaises(ValueError):
            s104 = Square(5, 2, 3, 104)
            s104.update(size=3, x=-3)
