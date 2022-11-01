#!/usr/bin/python3
"""Define test base case"""
import unittest

from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_Noneinstance(self):
        # testing normal instance of the Base
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_no_argument(self):
        # Adding two more instances
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 3)
    
    def test_with_value_instance(self):
        # Passing a positive integer as a value
        b3 = Base(12)
        self.assertEqual(12, b3.id)

    def test_passNone(self):
        # Passing a None as argument
        b4 = Base(None)
        self.assertEqual(b4.id, 4)

    def test_set_avalue(self):
        b = Base()
        b.id = 15
        self.assertEqual(b.id, 15)

    def test_string(self):
        bs1 = Base("Hello World")
        self.assertEqual(bs1.id, "Hello World")
    
    def test_set_string(self):
        bs1 = Base()
        bs1.id = "ALX SE"
        self.assertEqual(bs1.id, "ALX SE")
    
    def test_complex_number(self):
        b_complex = Base(complex(2,2))
        self.assertEqual(b_complex.id, 2 + 2j)

    def test_assign_class_private_Attri(self):
        with self.assertRaises(AttributeError):
            b_p_attr = Base(100).__nb_objects
