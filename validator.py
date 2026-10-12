"""Validation functions used in the DevOps control-work example."""

import re


def validate_email(email: str) -> bool:
    """Validate an email address using the template's basic pattern."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.fullmatch(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate a Russian phone number in the +7XXXXXXXXXX format."""
    pattern = r'^\+?7\d{10}$'
    normalized = phone.replace('-', '').replace(' ', '')
    return bool(re.fullmatch(pattern, normalized))


def validate_snils(snils: str) -> bool:
    """Validate the SNILS format and checksum."""
    cleaned = snils.replace('-', '').replace(' ', '')
    if not re.fullmatch(r'\d{11}', cleaned):
        return False

    digits = [int(digit) for digit in cleaned[:9]]
    checksum = int(cleaned[9:])
    calculated = sum((9 - index) * digit for index, digit in enumerate(digits))

    if calculated < 100:
        expected = calculated
    elif calculated % 101 == 100:
        expected = 0
    else:
        expected = calculated % 101

    return expected == checksum
