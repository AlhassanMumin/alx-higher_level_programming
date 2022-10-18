#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_defaultOne(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4) 

    def test_defaultTwo(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_emptyList(self):
        self.assertEqual(max_integer([]), None)

    def test_withNegative(self):
        self.assertAlmostEqual(max_integer([1, 3, -4, 29, -37]), 29)

    def test_withFloats(self):
        self.assertEqual(max_integer([1.3379, 0.03, -4.433, 2.32]), 2.32)

    def test_withInfinite(self):
        self.assertAlmostEqual(max_integer([1, 3, 4, 2, float('inf')]), float('inf'))

