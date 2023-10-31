#!/usr/bin/python3
"""
using unittest module to test max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    provides various test cases for max_integer()
    """

    def test_docs(self):
        """
        checks for proper documentation
        """
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_right_type(self):
        """
        test cases for right param type (list)
        """
        self.assertEqual(max_integer([3, 5, 9, 3, 8]), 9)
        self.assertEqual(max_integer([9, 10, 299, 3]), 299)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([7, 2]), 7)
        self.assertEqual(max_integer([-3, -2, -8, -200]), -2)

    def test_wrong_type(self):
        """
        test cases for wrong param types
        """
        self.assertRaises(TypeError, max_integer, '[2, 4, 8, 9]')
        self.assertRaises(TypeError, max_integer, (3, 10, 12, 9, 8))
        self.assertRaises(TypeError, max_integer, 7)
        self.assertRaises(TypeError, max_integer, ['1', 2, 3, 'four'])
