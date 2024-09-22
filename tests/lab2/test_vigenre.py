from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere
import unittest

class Test_Vigenre(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"),'LXFOPVEFRNHR')
        self.assertEqual(encrypt_vigenere("ALINAGAIDUK", "ME"), "MPURMKMMPYW")
        self.assertEqual(encrypt_vigenere("HELLO", "WORLD"), "DSCWR")

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("KITTY", "CAT"), "IIARY")
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), 'PYTHON')
        self.assertEqual(decrypt_vigenere("python", "a"), 'python')
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"),'ATTACKATDAWN')
        self.assertEqual(decrypt_vigenere("ilovepython", "yes"), "khwxaxappqj")

if __name__ == '__main__':
    unittest.main()