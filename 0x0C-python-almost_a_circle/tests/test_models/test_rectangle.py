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
        self.assertEqual(r1.id, 13)  # id = 9
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

    # id corresponde al valor de r
    def test_area(self):
        r34 = Rectangle(3, 10, 5, 4, 34)
        self.assertEqual(r34.area(), 30)

    def test_display0(self):
        r35 = Rectangle(3, 5, 4, 3, 35)
        self.assertEqual(r35.display(), None)

    def test_display1(self):
        r36 = Rectangle(3, 4, 2, 3)
        self.assertEqual(r36.id, 7)  # id 7
        self.assertEqual(r36.display(), None)

    # str
    def test_str1(self):
        r36 = Rectangle(4, 6, 2, 1, 36)
        self.assertEqual(r36.__str__(), "[Rectangle] (36) 2/1 - 4/6")

    def test_str2(self):
        r37 = Rectangle(5, 5, 1)  # id 10
        self.assertEqual(r37.id, 10)
        self.assertEqual(print(r37), None)
        self.assertEqual(r37.__str__(), "[Rectangle] (10) 1/0 - 5/5")

    def test_update0(self):
        r38 = Rectangle(10, 10, 10, 10, 38)
        r38.update(1000, 2)
        self.assertEqual(r38.__str__(), "[Rectangle] (1000) 10/10 - 2/10")
        r38.update(1000, 2, 3, 4, 5, 7)
        self.assertEqual(r38.__str__(), "[Rectangle] (1000) 4/5 - 2/3")
        r38.update()
        self.assertEqual(r38.__str__(), "[Rectangle] (1000) 4/5 - 2/3")
        r38.update(1000, 2, 18, 4, 5)
        self.assertEqual(r38.__str__(), "[Rectangle] (1000) 4/5 - 2/18")

    def test_update1(self):
        r39 = Rectangle(5, 4, 3, 2, 39)
        r39.update(2020, 3)
        self.assertEqual(r39.__str__(), "[Rectangle] (2020) 3/2 - 3/4")
        r39.update(height=1)
        self.assertEqual(r39.__str__(), "[Rectangle] (2020) 3/2 - 3/1")
        r39.update(width=1, x=2)
        self.assertEqual(r39.__str__(), "[Rectangle] (2020) 2/2 - 1/1")
        r39.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r39.__str__(), "[Rectangle] (2020) 1/3 - 4/2")
        r39.update(2021, 10, height=15)
        self.assertEqual(r39.__str__(), "[Rectangle] (2021) 1/3 - 10/2")

    # errors for update
    def test_updateNegativeValue(self):
        with self.assertRaises(ValueError):
            r200 = Rectangle(5, 4, 3, 2, 2300)
            r200.update(720, -3)
        with self.assertRaises(ValueError):
            r200 = Rectangle(5, 4, 3, 2)
            r200.update(720, -3)

        with self.assertRaises(ValueError):
            r200 = Rectangle(5, 4, 3, 2, 200)
            r200.update(x=20, y=-3)

        # error for check the order in the dictionary
        with self.assertRaises(TypeError):
            r200 = Rectangle(5, 4, 3, 2, 300)
            r200.update(x="hola", y=-3)
        # checking the order for errors
        with self.assertRaises(TypeError):
            r200 = Rectangle(5, 4, 3, 2, 301)
            r200.update(y=-3, x="hola")

    # id no corresponde al valor de r
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
