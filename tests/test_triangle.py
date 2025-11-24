import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(10, 2), 10)
        self.assertEqual(area(6, 4), 12)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 6), 16)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 0, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, 0)

    def test_triangle_inequality(self):
        with self.assertRaises(ValueError):
            perimeter(10, 2, 3)

        with self.assertRaises(ValueError):
            perimeter(1, 1, 3)

        with self.assertRaises(ValueError):
            perimeter(2, 3, 10)

    def test_area_both_negative(self):
        with self.assertRaises(ValueError):
            area(-5, -10)
