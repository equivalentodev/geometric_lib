import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(10, 10), 100)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(5, 5), 20)
        
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-2, 3)
        with self.assertRaises(ValueError):
            area(2, -3)

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            area(0, 5)
        with self.assertRaises(ValueError):
            area(5, 0)

    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(-2, 3)
        with self.assertRaises(ValueError):
            perimeter(2, -3)
        with self.assertRaises(ValueError):
            perimeter(0, 5)
