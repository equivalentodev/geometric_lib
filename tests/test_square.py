import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(1), 1)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(1), 4)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-3)

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            area(0)
        with self.assertRaises(ValueError):
            perimeter(0)
