import unittest
from iban_validator import validate_iban

class TestIBANValidation(unittest.TestCase):

    def test_1_valid_french_iban_with_spaces(self):
        # 1) Un IBAN français valide avec espaces
        self.assertTrue(validate_iban("FR76 3000 6000 0112 3456 7890 189"))

    def test_2_valid_french_iban_lowercase_no_spaces(self):
        # 2) Le même IBAN sans espaces ni majuscules
        self.assertTrue(validate_iban("fr7630006000011234567890189"))

    def test_3_invalid_key(self):
        # 3) Une clé invalide (changement de FR76 en FR77)
        self.assertFalse(validate_iban("FR77 3000 6000 0112 3456 7890 189"))

    def test_4_invalid_fr_length(self):
        # 4) Un IBAN FR de mauvaise longueur (26 caractères au lieu de 27)
        self.assertFalse(validate_iban("FR763000600001123456789018"))

    def test_5_contains_special_character(self):
        # 5) Une chaîne contenant un caractère spécial (@)
        self.assertFalse(validate_iban("FR76 3000 6000 0112 3456 7890 18@"))

if __name__ == '__main__':
    unittest.main()