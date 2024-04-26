import unittest
from models.square import Square
import os


class TestSquare(unittest.TestCase):

    def test_square_area(self):
        """
        Test calculating the area of a square.
        """
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_square_str_representation(self):
        """
        Test str representation of square.
        """
        square = Square(5)
        square.id = 1  # Set id explicitly to 1
        self.assertEqual(str(square), "[Square] (1) 0/0 - 5")

    def test_square_update(self):
        """
        Test updating square attributes.
        """
        square = Square(5)
        square.update(**{'id': 2, 'size': 3})
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 3)
    
    def test_constructor(self):
        """Test of Square() exists"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_string(self):
        """Test of Square("1") exists"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_string(self):
        """Test of Square(1, "2") exists"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_string(self):
        """Test of Square(1, 2, "3") exists"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_negative(self):
        """Test of Square(-1) exists"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative(self):
        """Test of Square(1, -2) exists"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        """Test of Square(1, 2, -3) exists"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero_size(self):
        """Test of Square(0) exists"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_to_dictionary(self):
        """Test of to_dictionary() in Square exists"""
        s = Square(5)
        expected = {'id': 25, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected)

    def test_create_id(self):
        """Test of Square.create(**{ 'id': 89 }) in Square exists"""
        s = Square.create(id=89)
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1 }) in Square exists"""
        s = Square.create(id=89, size=1)
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists"""
        s = Square.create(id=89, size=1, x=2)
        self.assertEqual(s.x, 2)

    def test_create_id_size_x_y(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists"""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.y, 3)

    def test_save_to_file_None(self):
        """Test of Square.save_to_file(None) in Square exists"""
        Square.save_to_file(None)
        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(),'[]')

    def test_save_to_file_empty_list(self):
        """Test of Square.save_to_file([]) in Square exists"""
        Square.save_to_file([])
        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_list_with_square(self):
        """Test of Square.save_to_file([Square(1)]) in Square exists"""
        s = Square(1)
        Square.save_to_file([s])
        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), '[{"id": 21, "size": 1, "x": 0, "y": 0}]')

    def test_load_from_file_no_file(self):
        """Test of Square.load_from_file() when file doesn’t exist exists"""
        os.remove('Square.json')
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        """Test of Square.load_from_file() when file exists exists"""
        s = Square(1)
        Square.save_to_file([s])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)



if __name__ == "__main__":
    unittest.main()
