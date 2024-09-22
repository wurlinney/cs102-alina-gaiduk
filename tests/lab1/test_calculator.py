import unittest
from unittest.mock import patch
import sys
from src.lab1.calculator import calc

class TestCalc(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calc(2.0, "+", 3.0), "2.0 + 3.0 = 5.0")

    def test_subtraction(self):
        self.assertEqual(calc(5.0, "-", 3.0), "5.0 - 3.0 = 2.0")

    def test_multiplication(self):
        self.assertEqual(calc(4.0, "*", 3.0), "4.0 * 3.0 = 12.0")

    def test_division(self):
        self.assertEqual(calc(10.0, "/", 2.0), "10.0 / 2.0 = 5.0")

    def test_zero_division(self):
        self.assertEqual(calc(5.0, '/', 0), 'На ноль делить нельзя.')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calc(3.0, '^', 2.0)

if __name__ == "__main__":
    unittest.main()