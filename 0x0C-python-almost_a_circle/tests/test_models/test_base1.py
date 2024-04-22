import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_assignment_with_none(self):
        """
        Test that id is assigned correctly when no argument is provided.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)  # Verify id is 1 for the first instance

        b2 = Base()
        self.assertEqual(b2.id, 2)  # Verify id increments for the second instance

    def test_id_assignment_with_value(self):
        """
        Test that id is assigned correctly using the provided argument.
        """
        b3 = Base(10)
        self.assertEqual(b3.id, 10)  # Verify custom id is assigned
    def test_to_json_string(self):
        b4 = Base()
        self.assertEqual(b4.to_json_string([]),"[]")
if __name__ == "__main__":
    unittest.main()

