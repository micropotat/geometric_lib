import unittest
import rectangle

class TestRectangle(unittest.TestCase):
    
    def test_area_positive_numbers(self):
        """Тест площади с положительными числами"""
        self.assertEqual(rectangle.area(5, 3), 15)
        self.assertEqual(rectangle.area(2, 2), 4)
        self.assertEqual(rectangle.area(10, 1), 10)
    
    def test_area_zero_values(self):
        """Тест площади с нулевыми значениями"""
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)
    
    def test_area_negative_numbers(self):
        """Тест площади с отрицательными числами (должны вызывать исключение)"""
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)
        with self.assertRaises(ValueError):
            rectangle.area(5, -1)
        with self.assertRaises(ValueError):
            rectangle.area(-2, -3)
    
    def test_area_float_numbers(self):
        """Тест площади с дробными числами"""
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(rectangle.area(3.14, 2.0), 6.28)
    
    def test_perimeter_positive_numbers(self):
        """Тест периметра с положительными числами"""
        self.assertEqual(rectangle.perimeter(5, 3), 16)
        self.assertEqual(rectangle.perimeter(2, 2), 8)
        self.assertEqual(rectangle.perimeter(10, 1), 22)
    
    def test_perimeter_zero_values(self):
        """Тест периметра с нулевыми значениями"""
        self.assertEqual(rectangle.perimeter(0, 5), 10)
        self.assertEqual(rectangle.perimeter(5, 0), 10)
        self.assertEqual(rectangle.perimeter(0, 0), 0)
    
    def test_perimeter_negative_numbers(self):
        """Тест периметра с отрицательными числами (должны вызывать исключение)"""
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, 5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(5, -1)
    
    def test_perimeter_float_numbers(self):
        """Тест периметра с дробными числами"""
        self.assertAlmostEqual(rectangle.perimeter(2.5, 4.0), 13.0)
        self.assertAlmostEqual(rectangle.perimeter(3.14, 2.0), 10.28)