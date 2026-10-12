import unittest

from validator import validate_phone


class PhoneValidationTests(unittest.TestCase):
    def test_accepts_russian_mobile_number(self):
        self.assertTrue(validate_phone("+79991234567"))

    def test_accepts_number_with_separators(self):
        self.assertTrue(validate_phone("7 999-123-45-67"))

    def test_rejects_eight_prefix(self):
        self.assertFalse(validate_phone("89991234567"))

    def test_rejects_wrong_length(self):
        self.assertFalse(validate_phone("+7999123"))

    def test_rejects_letters(self):
        self.assertFalse(validate_phone("+7ABCDEFGHIJ"))


if __name__ == "__main__":
    unittest.main()
