#!/usr/bin/python3
"""TestRectangle class"""
import unittest
from models.rectangle import Rectangle, Base
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Testing Rectangle class
        Testing objects and output errors
    Args:
        unittest ([type]): class to unittest in python
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_works(self):
        """simple test to check it is creating instances properly
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)  # id = 14
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        # area
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r2.id, 2)  # id 2
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        # area
        self.assertEqual(r2.area(), 20)

    # id corresponde al valor de r
    def test_area(self):
        """testing area in rectangles
        """
        r34 = Rectangle(3, 10, 5, 4, 34)
        self.assertEqual(r34.area(), 30)

    def test_display0(self):
        """testing the output of display to stdout
        It must print a rectangle of the same area given by width and height
        """
        r35 = Rectangle(3, 5, 4, 3, 35)
        #self.assertEqual(r35.display(), None)
        r300 = Rectangle(3, 2)
        display_exmp = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r300.display()
        self.assertEqual(fakeOutput.getvalue(), display_exmp)

    def test_display1(self):
        """testing the x and y values for display
        """
        r36 = Rectangle(3, 4, 2, 3)
        # id 7
        #self.assertEqual(r36.display(), None)
        r301 = Rectangle(3, 2, 2, 1, 301)
        display_exmp = "\n  ###\n  ###\n"

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r301.display()
        self.assertEqual(fakeOutput.getvalue(), display_exmp)

    def test_str1(self):
        """Checking if is printing in the correct format
        """
        r36 = Rectangle(4, 6, 2, 1, 36)
        self.assertEqual(
            r36.__str__(), "[Rectangle] ({}) 2/1 - 4/6".format(r36.id))

    def test_str2(self):
        """checking format string to the print
        """
        r37 = Rectangle(5, 5, 1)  # id 10
        #self.assertEqual(print(r37), None)
        self.assertEqual(
            r37.__str__(), "[Rectangle] ({}) 1/0 - 5/5".format(r37.id))

    def test_update0(self):
        """Checking the update per function with *args
        """
        r38 = Rectangle(10, 10, 10, 10, 38)
        r38.update(1000, 2)
        self.assertEqual(
            r38.__str__(), "[Rectangle] ({}) 10/10 - 2/10".format(r38.id))
        r38.update(1000, 2, 3, 4, 5, 7)
        self.assertEqual(
            r38.__str__(), "[Rectangle] ({}) 4/5 - 2/3".format(r38.id))
        r38.update()
        self.assertEqual(
            r38.__str__(), "[Rectangle] ({}) 4/5 - 2/3".format(r38.id))
        r38.update(1000, 2, 18, 4, 5)
        self.assertEqual(
            r38.__str__(), "[Rectangle] ({}) 4/5 - 2/18".format(r38.id))

    def test_update1(self):
        """checking the update with the *kwargs
        """
        r39 = Rectangle(5, 4, 3, 2, 39)
        r39.update(2020, 3)
        self.assertEqual(
            r39.__str__(), "[Rectangle] ({}) 3/2 - 3/4".format(r39.id))
        r39.update(height=1)
        self.assertEqual(
            r39.__str__(), "[Rectangle] ({}) 3/2 - 3/1".format(r39.id))
        r39.update(width=1, x=2)
        self.assertEqual(
            r39.__str__(), "[Rectangle] ({}) 2/2 - 1/1".format(r39.id))
        r39.update(x=1, height=2, y=3, width=4)
        self.assertEqual(
            r39.__str__(), "[Rectangle] ({}) 1/3 - 4/2".format(r39.id))
        r39.update(2021, 10, height=15)
        self.assertEqual(
            r39.__str__(), "[Rectangle] ({}) 1/3 - 10/2".format(r39.id))

    # errors for update
    def test_updateNegativeValue(self):
        """updating to negative values and checking the error message
        """
        with self.assertRaises(ValueError):
            r200 = Rectangle(5, 4, 3, 2, 2300)
            r200.update(720, -3)
        with self.assertRaises(ValueError):
            r200 = Rectangle(5, 4, 3, 2)
            r200.update(720, -3)

        with self.assertRaises(ValueError) as cm200:
            r200 = Rectangle(5, 4, 3, 2, 200)
            r200.update(x=20, y=-3)
        self.assertTrue("y must be >= 0" in str(cm200.exception))

        with self.assertRaises(TypeError) as cm:
            Rectangle("hi", 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        # error for check the order in the dictionary
        with self.assertRaises(TypeError) as cm201:
            r200 = Rectangle(5, 4, 3, 2, 300)
            r200.update(x="hola", y=-3)
        self.assertTrue("x must be an integer" in str(cm201.exception))
        # checking the order for errors
        with self.assertRaises(TypeError):
            r200 = Rectangle(5, 4, 3, 2, 301)
            r200.update(y=-3, x="hola")

    # todictionary

    def testRectangletodictionary(self):
        """testing todictionary method
        """
        r1 = Rectangle(10, 2, 1, 9, 203)
        self.assertEqual(r1.to_dictionary(), {
            'width': 10, 'x': 1, 'height': 2, 'y': 9, 'id': 203})
        r1.update(204, 20, 15, 20, 3)
        self.assertEqual(r1.to_dictionary(), {
            'width': 20, 'x': 20, 'height': 15, 'y': 3, 'id': 204})
        self.assertTrue(type(r1.to_dictionary()) is dict)

    # id no corresponde al valor de r
    def test_None(self):
        """testing in case of None
        """
        with self.assertRaises(TypeError):
            r3 = Rectangle(None, 2, 3, 4, 14)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, None, 3, 4, 16)

    def test_negative(self):
        """testing negative values
        """
        with self.assertRaises(ValueError):
            r5 = Rectangle(-10, 2, -3, 4, 17)

        with self.assertRaises(ValueError):
            r6 = Rectangle(-10, 2, "hola", 4, 18)

        with self.assertRaises(TypeError) as cm7:
            r7 = Rectangle(10, 2, 3, -4.5, 19)
        self.assertTrue("y must be an integer" in str(cm7.exception))
        with self.assertRaises(TypeError):
            r8 = Rectangle(10, -3.5)
            r8.id

    def test_positive_and0(self):
        """testing positive values
        """
        with self.assertRaises(TypeError):
            r9 = Rectangle(10.5, 2, -3, 4, 20)

        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 2, 3, "hola", 21)
        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 2, 3, 5, 22)
        with self.assertRaises(ValueError):
            r12 = Rectangle(10, 0, 3, "hola", 23)

    def test_bool(self):
        """tsting bool case
        """
        with self.assertRaises(TypeError):
            r12 = Rectangle(bool, 2, -3, 4, 24)
        with self.assertRaises(TypeError):
            r13 = Rectangle(10, bool, -3, 4, 25)

    def test_tuple(self):
        """testing tuple
        """
        with self.assertRaises(TypeError):
            r14 = Rectangle(10, 2, (1, 2), 4, 26)
        with self.assertRaises(ValueError):
            r15 = Rectangle(10, -2, (-3, 10))  # id = 7

    def test_list(self):
        """testing list
        """
        with self.assertRaises(TypeError):
            r14 = Rectangle(10, 2, [1, 2], 4, 27)
        with self.assertRaises(ValueError):
            r15 = Rectangle(10, -2, [-3, 10], 28)  # id = 8

    def test_dict(self):
        """testing dictionaries
        """
        with self.assertRaises(TypeError):
            r16 = Rectangle(10, 2, {1, 2}, 4, 29)
        with self.assertRaises(TypeError):
            r17 = Rectangle(10, {-3, 10}, -2, 30)  # id = 9
        with self.assertRaises(ValueError):
            r18 = Rectangle(10, -2, {-3, 10}, 31)  # id = 10

    def test_string(self):
        """testing strings
        """
        with self.assertRaises(TypeError):
            r19 = Rectangle(10, "hola", "holberton", 4, 32)
        with self.assertRaises(TypeError):
            r20 = Rectangle("string", 12, -3, 4, 33)

    def test_empty(self):
        """testing empty cases
        """
        with self.assertRaises(TypeError):
            r21 = Rectangle()
