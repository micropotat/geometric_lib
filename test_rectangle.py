import unittest
import rectangle

class TestRectangle(unittest.TestCase):
    
    def test_area_positive(self):
        self.assertEqual(rectangle.area(5, 3), 15)
        self.assertEqual(rectangle.area(2, 2), 4)
    
    def test_area_zero(self):
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)
        with self.assertRaises(ValueError):
            rectangle.area(5, -1)
    
    def test_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(5, 3), 16)
        self.assertEqual(rectangle.perimeter(2, 2), 8)
    
    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 5), 10)
        self.assertEqual(rectangle.perimeter(5, 0), 10)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, 5)
