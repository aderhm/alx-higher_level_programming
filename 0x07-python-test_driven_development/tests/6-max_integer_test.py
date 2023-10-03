#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)
        self.assertEqual(max_integer("Brennan"), 'r')
        self.assertEqual(max_integer(["Brennan", "is", "my", "name"]), "name")
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
