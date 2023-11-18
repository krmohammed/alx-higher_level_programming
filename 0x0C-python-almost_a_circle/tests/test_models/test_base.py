#!/usr/bin/python3
"""
unittest for base class
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseInit(unittest.TestCase):
    """
    test cases for init method
    """

    def test_no_argument(self):
        a = Base()
        b = Base()
        self.assertFalse(a.id == b.id)
        self.assertEqual(a.id, b.id - 1)

    def test_one_argument(self):
        a = Base(3)
        b = Base(5)
        self.assertEqual(a.id, b.id - 2)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            a = Base(8, 9)

    def test_non_int(self):
        a = Base([2, 4, 6])
        b = Base({'me': 9})
        self.assertEqual([2, 4, 6], a.id)
        self.assertTrue({'me': 9} == b.id)
        self.assertEqual(Base(3.9).id, 3.9)
        self.assertTrue(Base('her').id, 'her')
        self.assertEqual(Base((2, 3, 5)).id, (2, 3, 5))
        self.assertTrue(Base({8, 9, 10}), {8, 9, 10})

    def test_infinity(self):
        c = Base('inf')
        self.assertTrue(float(c.id) == float('inf'))

    def test_nan(self):
        c = Base(float('nan'))
        self.assertTrue(type(c.id) == float)

    def test_other_types(self):
        self.assertEqual(Base(-4).id, -4)
        self.assertTrue(Base(0).id == 0)
        self.assertTrue(Base(False).id == False)

class Test_ToJSON_String(unittest.TestCase):
    """
    test cases for the function to_json_string()
    """

    def test_correct(self):
        d = {'me': 2, 'you': 4}
        a = Base.to_json_string([d])
        self.assertTrue(f'[{d}]', a)

    def test_empty_none(self):
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


if __name__ == '__main__':
    unittest.main()
