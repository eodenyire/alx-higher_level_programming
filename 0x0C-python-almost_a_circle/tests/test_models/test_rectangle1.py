import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        # Test initialization of Rectangle instance
        rect = Rectangle(5, 10, 1, 1, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.id, 1)

    def test_area(self):
        # Test area calculation
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        # Test display method
        rect = Rectangle(4, 3)
        self.assertEqual(rect.display(), None)  # Check if it returns None (for simplicity)

    def test_str(self):
        # Test __str__ method
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_update(self):
        # Test update method
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(2, 6, 12, 4, 5)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)
        self.assertEqual(rect.id, 2)

    def test_to_dictionary(self):
        # Test to_dictionary method
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3})

if __name__ == '__main__':
    unittest.main()

