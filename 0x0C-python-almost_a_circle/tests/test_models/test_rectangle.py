import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle
import os


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

    def test_update_kwargs(self):
        r1 = Rectangle(4, 5, 1, 2, 10)
        r1.update(**{'id': 20, 'width': 6, 'height': 7, 'x': 8, 'y': 9})
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 9)


    def test_constructor(self):
        """Test of Rectangle("1", 2) exists"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_constructor_width_string(self):
        """Test of Rectangle(1, "2") exists"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_constructor_height_string(self):
        """Test of Rectangle(1, 2, "3") exists"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_constructor_width_negative(self):
        """Test of Rectangle(-1, 2) exists"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_constructor_height_negative(self):
        """Test of Rectangle(1, -2) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_constructor_width_zero(self):
        """Test of Rectangle(0, 2) exists"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_constructor_height_zero(self):
        """Test of Rectangle(1, 0) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_constructor_x_negative(self):
        """Test of Rectangle(1, 2, -3) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_constructor_y_negative(self):
        """Test of Rectangle(1, 2, 3, -4) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_create_id(self):
        """Test of Rectangle.create(**{ 'id': 89 }) in Rectangle exists"""
        r = Rectangle.create(id=89)
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1 }) in Rectangle exists"""
        r = Rectangle.create(id=89, width=1)
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists"""
        r = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists"""
        r = Rectangle.create(id=89, width=1, height=2, x=3)
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists"""
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.y, 4)

    def test_save_to_file_None(self):
        """Test of Rectangle.save_to_file(None) in Rectangle exists"""
        Rectangle.save_to_file(None)
        with open('Rectangle.json','r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_empty_list(self):
        """Test of Rectangle.save_to_file([]) in Rectangle exists"""
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(),'[]')

    def test_save_to_file_list_with_rectangle(self):
        """Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle exists"""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[{"id": 13, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file_no_file(self):
        """Test of Rectangle.load_from_file() when file doesn’t exist exists"""
        os.remove('Rectangle.json')
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_file_exists(self):
        """Test of Rectangle.load_from_file() when file exists exists"""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
