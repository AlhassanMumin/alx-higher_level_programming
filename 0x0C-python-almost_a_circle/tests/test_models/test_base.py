#!/usr/bin/python3
"""Define test base case"""
import unittest

from models.base import Base


class TestBaseClassForInstances(unittest.TestCase):
    """The test case class"""

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
        b_complex = Base(complex(2, 2))
        self.assertEqual(b_complex.id, 2 + 2j)

    def test_assign_class_private_Attri(self):
        with self.assertRaises(AttributeError):
            b_p_attr = Base(100).__nb_objects

    def test_float(self):
        self.assertEqual(3.4, Base(3.4).id)

    def test_boolean(self):
        self.assertEqual(True, Base(True).id)

    def test_dictionary(self):
        self.assertEqual({'1':1, '2':2}, Base({'1':1, '2':2}).id)

    def test_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple(self):
        self.assertEqual((1, 4), Base((1, 4)).id)

    def test_bytes(self):
        self.assertEqual(bytes(3), Base(b'\x00\x00\x00').id)
    
    def test_byteArray(self):
        self.assertEqual(bytearray(3), Base((b'\x00\x00\x00')).id)

    def test_memoryview(self):
        self.assertEqual(memoryview(b"ALX SE"), Base(memoryview(b"ALX SE")).id)

    def test_more_than_1arg(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Base(1, 2).id, all(1, 2))

    def test_infinite(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_NaN(self):
        self.assertNotEqual(Base(float('nan')).id, float('nan'))


