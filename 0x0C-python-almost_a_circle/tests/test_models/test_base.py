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
            # Check if the file contains only one line with the string '[]'
            self.assertEqual(['[]'], f.readlines())
        self.assertEqual(Base.load_from_file_csv(), [])

        # Remove the temporary CSV file
     
        os.remove("Base.csv")

    def test_constructor(self):
        """Test of Base() for assigning automatically an ID exists"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_constructor_increment(self):
        """Test of Base() for assigning automatically an ID + 1 of the previous exists"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_None(self):
        """Test of Base.to_json_string(None) exists"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test of Base.to_json_string([]) exists"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_dict(self):
        """Test of Base.to_json_string([ { 'id': 12 }]) exists"""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_None(self):
        """Test of Base.from_json_string(None) exists"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """Test of Base.from_json_string("[]") exists"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_data(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') exists"""
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])        

if __name__ == "__main__":
    unittest.main()

