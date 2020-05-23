#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):

    def test_max_positive(self):
        """test_max_positive
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_max_negative(self):
        """test_max_negative
        """
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertAlmostEqual(max_integer([-2]), -2)

    def test_mix_values(self):
        """test_mix_values
        """
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_none(self):
        "test_none"
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer([]), None)
        self.assertAlmostEqual(max_integer([0]), 0)

    def test_float(self):
        "test_float"
        self.assertAlmostEqual(max_integer([1.4, 2.2, 3.2, 4.1]), 4.1)
        self.assertAlmostEqual(max_integer([-5.3, -3, -1.2]), -1.2)
