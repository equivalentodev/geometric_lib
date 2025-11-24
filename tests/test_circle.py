import unittest
from circle import area, perimeter
import math

class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), math.pi * 4)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-3)
        with self.assertRaises(ValueError):
            perimeter(-3)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            area(0)
        with self.assertRaises(ValueError):
            perimeter(0)
