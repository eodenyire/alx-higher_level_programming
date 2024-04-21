import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Reset __nb_objects to 0 before running tests.
        """
        Base.__nb_objects = 0

    def test_id_assignment_with_none(self):
        """
        Test that id is assigned correctly when no argument is provided.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)  # Verify id is 1 for the first instance

        b2 = Base()
        self.assertEqual(b2.id, 2)  # Verify id increments for the second instance

    # ... other test cases

if __name__ == "__main__":
    unittest.main()

