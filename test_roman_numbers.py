#! /usr/bin/python


"""
Tests case for roman_number.py
"""

import unittest
from roman_numbers import *


CORRECT_RESULTS = [
        ('XXXIX', 39),
        ('CCXLVI', 246),
        ('MMCDXXI', 2421),
        ('CLX', 160),
        ('CCVII', 207),
        ('MLXVI', 1066),
        ('MMXIV', 2014),
        ('MMXIX', 2019),
        ('XCIX', 99)
]

WRONG_ROMAN = [
    'IC',
    'XD',
    'IIII',
    'XXXX',
    'XIXI',
    'CIDI',
    'CCM'
]


class TestIsValidRoman(unittest.TestCase):
    """
    Test that is_valid_roman actualy finds
    correct and wrong roman numerals
    """

    def full_regex(self, upper):
        """
        Generate all Roman Numerals
        from 1 up to 9999 and run the check
        against them
        """
        for i in range(1, 10000):
            roman = int_to_roman(i, upper=upper)
            self.assertTrue(is_valid_roman(roman), roman)

    def test_full_upper(self):
        """
        Test for upper case numerals
        """
        self.full_regex(True)

    def test_full_lower(self):
        """
        Test for lower case numerals
        """
        self.full_regex(False)

    def test_wrong(self):
        """
        Check that wrong values are rejected
        """
        for i in WRONG_ROMAN:
            self.assertFalse(is_valid_roman(i))


class TestIntToRoman(unittest.TestCase):
    """
    Test int to roman convertion.
    """

    def test_errors(self):
        """
        Check that wrong input raises
        an exception
        """
        for i in ['yt', 5.6, (4.5, 7)]:
            with self.assertRaises(ValueError):
                int_to_roman(i)
                int_to_roman(i, upper=False)

    def test_convertion(self):
        """
        Using a set of correct (roman, int) couples
        converts the integer and checks the result is
        correct
        """
        for roman, integer in CORRECT_RESULTS:
            self.assertEqual(int_to_roman(integer), roman)


class TestRomanToInt(unittest.TestCase):
    """
    Test Roman to integer conversion
    """

    def test_roman_to_int_value(self):
        """
        Using a set of correct (roman, int) couples
        converts the roman and checks the result is
        correct
        """
        for roman, integer in CORRECT_RESULTS:
            self.assertEqual(roman_to_int(roman), integer)

    def test_roman_to_int_error(self):
        """
        Check that wrong input raises
        an exception
        """
        for i in [45, 5.6, (6, '8')]:
            with self.assertRaises(ValueError):
                roman_to_int(i)

        for i in WRONG_ROMAN:
            with self.assertRaises(ValueError):
                roman_to_int(i)


class TestFullConvertion(unittest.TestCase):
    """
    Run a full convertion test:
        int -> roman -> int
    and checks that the two integers are equals
    """

    def full_convertion_run(self, upper):
        """
        Generate all possibile integers from 1 to 9999
        """
        for i in range(1, 10000):
            roman = int_to_roman(i, upper=upper)
            arabic = roman_to_int(roman)
            self.assertEqual(i, arabic)

    def test_full_convertion_lower(self):
        """
        Test lower case output
        """
        self.full_convertion_run(False)

    def test_full_convertion_upper(self):
        """
        Test upper case output
        """
        self.full_convertion_run(True)


if __name__ == "__main__":
    unittest.main()
