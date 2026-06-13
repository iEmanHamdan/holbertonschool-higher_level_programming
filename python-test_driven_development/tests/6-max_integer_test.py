#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittest cases for the max_integer function."""

    def test_ordered_list(self):
        """Tests an ordered list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Tests an unordered list of positive integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Tests a list where the maximum value is at the start."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Tests passing an empty list container."""
        self.assertIsNone(max_integer([]), None)

    def test_one_element_list(self):
        """Tests a list containing only a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative_numbers(self):
        """Tests a list completely comprised of negative integers."""
        self.assertEqual(max_integer([-1, -5, -3, -20]), -1)

    def test_mixed_positive_negative(self):
        """Tests a list with both positive and negative values."""
        self.assertEqual(max_integer([-10, 5, -2, 0, 3]), 5)

    def test_floats_and_integers(self):
        """Tests a list with mixed valid floats and integers."""
        self.assertEqual(max_integer([1.5, 2.7, 9.8, 4]), 9.8)


if __name__ == '__main__':
    unittest.main()
