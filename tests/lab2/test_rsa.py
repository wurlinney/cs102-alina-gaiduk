import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair
import random

class RSATest(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(56))
        self.assertTrue(is_prime(61))
        self.assertTrue(is_prime(47))
        self.assertFalse(is_prime(49))

    def test_gcd(self):
        self.assertEqual(gcd(30, 45), 15)
        self.assertEqual(gcd(50, 20), 10)
        self.assertEqual(gcd (15, 12), 3)
        self.assertEqual(gcd(16, 20), 4)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(3, 11), 4)
        self.assertEqual(multiplicative_inverse(10, 17), 12)
        self.assertEqual(multiplicative_inverse(17, 3120), 2753)
        self.assertEqual(multiplicative_inverse(121, 288), 169)

    def test_generate_keypair(self):
        random.seed(1234567)
        self.assertEqual(((121, 323), (169, 323)), generate_keypair(17, 19))
        self.assertEqual(((142169, 1697249), (734969, 1697249)), generate_keypair(1229, 1381))
        self.assertEqual(((9678731, 11188147), (1804547, 11188147)), generate_keypair(3259, 3433))

if __name__ == '__main__':
    unittest.main()