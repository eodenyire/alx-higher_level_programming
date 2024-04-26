#!/usr/bin/python3
"""Unittest for base class"""

import unittest
import json
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_create(self):
        """Test create method"""
        r1 = Base(98)
        self.assertEqual(r1.id, 98)

    def test_load_from_file(self):
        """Test load_from_file method"""
        Base.save_to_file([])
        self.assertEqual(Base.load_from_file(), [])

        Base.save_to_file(None)
        self.assertEqual(Base.load_from_file(), [])

    def test_save_to_file(self):
        """Test save_to_file method"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual([], json.load(f))

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as f:
            self.assertEqual([], f.readlines())

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        Base.save_to_file_csv([])
        self.assertEqual(Base.load_from_file_csv(), [])


if __name__ == "__main__":
    unittest.main()

