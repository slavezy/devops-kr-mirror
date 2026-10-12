import unittest

from validator import validate_email, validate_phone, validate_snils


class ValidatorTests(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid"))

    def test_validate_phone(self):
        self.assertTrue(validate_phone("+79991234567"))
        self.assertTrue(validate_phone("7 999-123-45-67"))
        self.assertFalse(validate_phone("89991234567"))
        self.assertFalse(validate_phone("+7999123"))

    def test_validate_snils(self):
        self.assertTrue(validate_snils("11223344595"))
        self.assertTrue(validate_snils("001-001-999 65"))
        self.assertFalse(validate_snils("123"))
        self.assertFalse(validate_snils("123456789012"))
        self.assertFalse(validate_snils("abcdefghijk"))
        self.assertFalse(validate_snils("11223344500"))


if __name__ == "__main__":
    unittest.main()
