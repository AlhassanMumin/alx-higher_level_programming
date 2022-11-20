#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""

import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Instance(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""
    
    def test_rectangle_is_Base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        r1 = Rectangle(12, 2)
        self.assertEqual(r1.id, 2)

    def test_without_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_two_args(self):
        r1 = Rectangle(4, 45)
        r = Rectangle(4, 45)
        r2 = Rectangle(4, 45)
        self.assertEqual(r1.id, r2.id - 2)

    def test_with_idvalue(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            h_string = Rectangle(4, "height")

    def test_set_negative_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(10, 2)
            r.width = -10

    def test_pass_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(10, 2, 3, -1)

    def test_set_x_as_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}

    def test_set_y_as_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2)
            r.y = {}

    def test_y_setter(self):
         r = Rectangle(5, 7, 7, 5, 1)
         self.assertEqual(5, r.y)

    def test_x_setter(self):
        r = Rectangle(2, 23)
        r.x = 2334
        self.assertEqual(2334, r.x)

    def test_rectangle_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    @staticmethod
    def capture_stdout(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_Instance.capture_stdout(r, "display")

        self.assertEqual(" ###\n ###\n", capture.getvalue())

if __name__ == '__main__':
    unittest.main()


