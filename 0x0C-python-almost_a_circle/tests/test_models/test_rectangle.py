#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleInstance(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_Base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        r1 = Rectangle(12, 2)
        self.assertEqual(r1.id, 2)
