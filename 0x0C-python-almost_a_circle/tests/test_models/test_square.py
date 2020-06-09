#!/usr/bin/python3
"""square tests"""
import unittest
from models.base import Base
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """Tests for Square class

    Args:
        unittest ([type]): Unittest for Square class
    """

    def setUp(self):
        """setting up intial conditions
        """
        Base._Base__nb_objects = 0

    def test_squareid(self):
        """adding test for id in square
        """
        s98 = Square(10, 5, 4)

        self.assertEqual(s98.id, 1)  # id 1

        s99 = Square(10, 6, 8)
        self.assertEqual(s99.id, 2)  # id 2

    # str for square

    def test_squarestr(self):
        """str for square
        """
        s101 = Square(5, 3, 2, 101)
        self.assertEqual(
            s101.__str__(), "[Square] ({}) 3/2 - 5".format(s101.id))
        s102 = Square(5, 0, 0)
        self.assertEqual(
            s102.__str__(), "[Square] ({}) 0/0 - 5".format(s102.id))  # id 17

    def testsquaredisplay(self):
        """test the display
        """
        s303 = Square(4, 2, 1, 303)
        display_exmp = "\n  ####\n  ####\n  ####\n  ####\n"

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            s303.display()
        self.assertEqual(fakeOutput.getvalue(), display_exmp)

    # update tests
    def test_squareupdate(self):
        """updating the square, and checking it
        """
        s103 = Square(5)
        self.assertEqual(
            s103.__str__(), "[Square] ({}) 0/0 - 5".format(s103.id))  # id 18
        s103.update(103)
        self.assertEqual(
            s103.__str__(), "[Square] ({}) 0/0 - 5".format(s103.id))
        s103.update(103, 2)
        self.assertEqual(
            s103.__str__(), "[Square] ({}) 0/0 - 2".format(s103.id))
        s103.update(103, 2, 3)
        self.assertEqual(
            s103.__str__(), "[Square] ({}) 3/0 - 2".format(s103.id))
        s103.update(103, 2, 3, 4)
        self.assertEqual(
            s103.__str__(), "[Square] ({}) 3/4 - 2".format(s103.id))
        s103.update(y=1)
        self.assertEqual(
            s103.__str__(), "[Square] (103) 3/1 - 2".format(s103.id))
        s103.update(size=7, id=4000, y=1)
        self.assertEqual(
            s103.__str__(), "[Square] ({}) 3/1 - 7".format(s103.id))

    def test_errorsupdate(self):
        """checking tests for erros in update function
        """
        with self.assertRaises(TypeError) as cm104:
            s104 = Square(5, 2, 3, 104)
            s104.update(x=-3, size="hola")
        self.assertTrue("width must be an integer" in str(cm104.exception))

        with self.assertRaises(ValueError):
            s104 = Square(5, 2, 3, 104)
            s104.update(size=3, x=-3)

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(2000, (None, ))

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(2000, [None])

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(2000, 3, (1, 2))

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(2000, 3, 2, True)

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(x=True)

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(y=[None], x=3)

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(y=None, x=3)

        with self.assertRaises(TypeError):
            s104 = Square(5, 2, 3, 104)
            s104.update(y=3, x=3, size=None)

    def test_squaretypevalue(self):
        """type of the square value
        """
        with self.assertRaises(TypeError):
            s105 = Square(5, "hola")

        with self.assertRaises(TypeError):
            s105 = Square([1], "hola", 3, 105)

        with self.assertRaises(TypeError):
            s106 = Square(True, 3, 3, 106)

        with self.assertRaises(TypeError):
            s107 = Square((1, 2), 3, 3, 107)

        with self.assertRaises(TypeError):
            s107 = Square({1, 2}, 3, 3, 107)

        with self.assertRaises(TypeError):
            s108 = Square(3.5, 3, 3, 108)

        with self.assertRaises(TypeError):
            s108 = Square("holberton", 3, 3, 108)

        with self.assertRaises(TypeError):
            s109 = Square(None, 3, 3, 109)

        with self.assertRaises(ValueError):
            s110 = Square(-3, 3, 3, 110)

        with self.assertRaises(TypeError):
            s110 = Square(3, {1, 2}, 3, 110)

        with self.assertRaises(TypeError):
            s111 = Square(3, 2, True, 111)

        with self.assertRaises(TypeError):
            s111 = Square("")

        with self.assertRaises(TypeError):
            s112 = Square()

    # to dictionary tests
    def testSquaretodictionary(self):
        """testing dictionary
        """
        s113 = Square(10, 2, 1, 113)
        self.assertEqual(s113.to_dictionary(), {
                         'id': 113, 'x': 2, 'size': 10, 'y': 1})
        s113.update(114, 20, 30, 40)
        self.assertEqual(s113.to_dictionary(), {
                         'id': 114, 'x': 30, 'size': 20, 'y': 40})
        self.assertTrue(type(s113.to_dictionary()) is dict)
