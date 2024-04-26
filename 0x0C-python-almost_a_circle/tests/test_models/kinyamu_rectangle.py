import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

    def test_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

    def test_display(self):
        r1 = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r1.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        r1 = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 1/2 - 4/5")

    def test_update(self):
        r1 = Rectangle(4, 5, 1, 2, 10)
        r1.update(20, 6, 7, 8, 9)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 9)

    def test_to_dictionary(self):
        r1 = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(r1.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

