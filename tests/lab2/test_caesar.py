import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar
import unittest

class Test_Caesar(unittest.TestCase):

    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(encrypt_caesar("Hello World", 5), "Mjqqt Btwqi")
        self.assertEqual(encrypt_caesar(""), "")
        self.assertEqual(encrypt_caesar("XY"), "AB")

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(decrypt_caesar("Tqxxa Iadxp", 12), "Hello World")
        self.assertEqual(decrypt_caesar("", 3), "")
        self.assertEqual(decrypt_caesar("AB", 1), "ZA")

if __name__ == '__main__':
    unittest.main()