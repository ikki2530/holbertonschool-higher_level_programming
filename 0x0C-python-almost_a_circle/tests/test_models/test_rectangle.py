#!/usr/bin/python3
"""TestRectangle class"""
import unittest
from models.rectangle import Rectangle, Base


class TestRectangle(unittest.TestCase):
    """Testing Rectangle class

    Args:
        unittest ([type]): [description]
    """

    def test_works(self):
        """simple test
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)  # id = 5
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        # area
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(10, 2, 0, 0, 13)
        self.assertEqual(r2.id, 13)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        # area
        self.assertEqual(r2.area(), 20)

    #id corresponde al valor de r
    def test_area(self):
        r34 = Rectangle(3, 10, 5, 4, 34)
        self.assertEqual(r34.area(), 30)

    def test_display0(self):
        r35 = Rectangle(3, 5, 4, 3, 35)
        self.assertEqual(r35.display(), None)

    #id no corresponde al valor de r
    def test_None(self):
        with self.assertRaises(TypeError):
            r3 = Rectangle(None, 2, 3, 4, 14)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, None, 3, 4, 16)

    def test_negative(self):
        with self.assertRaises(ValueError):
            r5 = Rectangle(-10, 2, -3, 4, 17)

        with self.assertRaises(ValueError):
            r6 = Rectangle(-10, 2, "hola", 4, 18)

        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 2, 3, -4.5, 19)

        with self.assertRaises(TypeError):
            r8 = Rectangle(10, -3.5)  # id = 6
            print(r8.id)

    def test_positive_and0(self):
        with self.assertRaises(TypeError):
            r9 = Rectangle(10.5, 2, -3, 4, 20)

        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 2, 3, "hola", 21)
        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 2, 3, 5, 22)
        with self.assertRaises(ValueError):
            r12 = Rectangle(10, 0, 3, "hola", 23)

    def test_bool(self):
        with self.assertRaises(TypeError):
            r12 = Rectangle(bool, 2, -3, 4, 24)
        with self.assertRaises(TypeError):
            r13 = Rectangle(10, bool, -3, 4, 25)

    def test_tuple(self):
        with self.assertRaises(TypeError):
            r14 = Rectangle(10, 2, (1, 2), 4, 26)
        with self.assertRaises(ValueError):
            r15 = Rectangle(10, -2, (-3, 10))  # id = 7

    def test_list(self):
        with self.assertRaises(TypeError):
            r14 = Rectangle(10, 2, [1, 2], 4, 27)
        with self.assertRaises(ValueError):
            r15 = Rectangle(10, -2, [-3, 10], 28)  # id = 8

    def test_dict(self):
        with self.assertRaises(TypeError):
            r16 = Rectangle(10, 2, {1, 2}, 4, 29)
        with self.assertRaises(TypeError):
            r17 = Rectangle(10, {-3, 10}, -2, 30)  # id = 9
        with self.assertRaises(ValueError):
            r18 = Rectangle(10, -2, {-3, 10}, 31)  # id = 10

    def test_string(self):
        with self.assertRaises(TypeError):
            r19 = Rectangle(10, "hola", "holberton", 4, 32)
        with self.assertRaises(TypeError):
            r20 = Rectangle("string", 12, -3, 4, 33)

    def test_empty(self):
        with self.assertRaises(TypeError):
            r21 = Rectangle()
