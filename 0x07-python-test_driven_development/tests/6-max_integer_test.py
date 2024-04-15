#!/usr/bin/python3
"""Unittest for max_integer([..])

This module contains unit tests for the max_integer function
from the 6-max_integer module. The tests cover various cases
to ensure the correct behavior of the max_integer function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Suite test for max_integer function"""

    # Test case for a list with positive and negative numbers
    def test_max_integer(self):
        """Test for finding the maximum integer in a list"""
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    # Test case for an empty list
    def test_empty_list(self):
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)

    # Test case for a list with repeated numbers
    def test_repeated_number(self):
        """Test for a list with repeated numbers"""
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    # Test case for a list with floating-point numbers
    def test_float_numbers(self):
        """Test for a list with floating-point numbers"""
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    # Test case for a list with a mathematical expression
    def test_max_operated_integer(self):
        """Test for a list with a mathematical expression"""
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    # Test case for a list with negative numbers
    def test_neg_numbers(self):
        """Test for a list with negative numbers"""
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    # Test case for a list with the maximum number at the beginning
    def test_max_at_beginning(self):
        """Test for a list with the maximum number at the beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    # Test case for a list with only zeros
    def test_zero_number(self):
        """Test for a list with only zeros"""
        self.assertEqual(max_integer([0, 0]), 0)

    # Test case for a big list
    def test_big_list(self):
        """Test for a big list"""
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    # Test case for a list with a loop
    def test_list_with_loop(self):
        """Test for a list with a loop"""
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    # Test case for a list with one number
    def test_one_number_in_a_list(self):
        """Test for a list with one number"""
        self.assertEqual(max_integer([1]), 1)

    # Test case for a list with a string number
    def test_string_number_in_a_list(self):
        """Test for a list with a string number"""
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    # Test case for a list with a tuple
    def test_tuple_in_a_list(self):
        """Test for a list with a tuple"""
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    # Test case for a dictionary
    def test_dictionary(self):
        """Test for a dictionary"""
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    # Test case for a number
    def test_number(self):
        """Test for a single number"""
        with self.assertRaises(TypeError):
            max_integer(1)

