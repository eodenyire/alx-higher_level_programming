import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_id_assignment_with_none(self):
        """
        Test that id is assigned correctly when no argument is provided.
        """
        Base._Base__nb_objects = 0  # Reset the counter
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)  # Verify id is 1 for the first instance
        self.assertEqual(b2.id, 2)  # Verify id increments for the second instance

    def test_id_assignment_with_value(self):
        """
        Test that id is assigned correctly using the provided argument.
        """
        b3 = Base(10)
        self.assertEqual(b3.id, 10)  # Verify custom id is assigned

    def test_to_json_string(self):
        """
        Test the serialization of a list of dictionaries to JSON.
        """
        b4 = Base()
        self.assertEqual(b4.to_json_string([]), "[]")

    def test_save_to_file(self):
        """
        Test saving objects to a JSON file.
        """
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            self.assertEqual(json.load(file), [b1.to_dictionary(), b2.to_dictionary()])
        os.remove("Base.json")

    def test_from_json_string(self):
        """
        Test deserialization of JSON string to a list of dictionaries.
        """
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_output = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    def test_create(self):
        """
        Test creating instances from dictionaries.
        """
        dictionary_r = {'height': 1, 'width': 4}
        obj = Rectangle.create(**dictionary)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.width, 4)

    @unittest.skip("Skipping test_draw since it requires a display environment.")
    def test_draw(self):
        """
        Test drawing rectangles and squares using turtle.
        """
        pass

    def test_load_from_file(self):
        """
        Test loading instances from a JSON file.
        """
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

    def test_save_to_file_csv(self):
        """
        Test saving objects to a CSV file.
        """
        b1 = Base()
        b2 = Base()
        Base.save_to_file_csv([b1, b2])
        with open("Base.csv", "r") as file:
            lines = file.readlines()
            self.assertEqual(lines[1].strip(), "1,1,0,0")  # Assuming Rectangle format
            self.assertEqual(lines[2].strip(), "2,1,0,0")  # Assuming Rectangle format
        os.remove("Base.csv")
"""
    def test_load_from_file_csv(self):
        """
        Test loading instances from a CSV file.
        """
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file_csv([b1, b2])
        loaded_objs = Base.load_from_file_csv()
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)
"""

if __name__ == "__main__":
    unittest.main()

