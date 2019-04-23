#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

"""
Tests case for roman_number.py
Test on int to roman and roman to int are run on safe
(with check on input variables) version.

To ensure that safe and fast version generates the
same output under controlled circumstances there
are the FullConversion (int -> roman -> int) tests.
"""

import unittest

from roman_numbers import int_to_roman, int_to_roman_safe
from roman_numbers import roman_to_int, roman_to_int_safe
from roman_numbers import is_valid_roman


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
            roman = int_to_roman_safe(i, upper=upper)
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
    This test is run only on safe version
    """

    def test_errors(self):
        """
        Check that wrong input raises
        an exception
        Here safe version is mandatory.
        """
        for i in ['yt', 5.6, (4.5, 7)]:
            with self.assertRaises(ValueError):
                int_to_roman_safe(i)
                int_to_roman_safe(i, upper=False)

    def test_convertion(self):
        """
        Using a set of correct (roman, int) couples
        converts the integer and checks the result is
        correct
        """
        for roman, integer in CORRECT_RESULTS:
            self.assertEqual(int_to_roman_safe(integer), roman)


class TestRomanToInt(unittest.TestCase):
    """
    Test Roman to integer conversion.
    This test is run only on safe version
    """

    def test_roman_to_int_value(self):
        """
        Using a set of correct (roman, int) couples
        converts the roman and checks the result is
        correct
        """
        for roman, integer in CORRECT_RESULTS:
            self.assertEqual(roman_to_int_safe(roman), integer)

    def test_roman_to_int_error(self):
        """
        Check that wrong input raises
        an exception
        """
        for i in [45, 5.6, (6, '8')]:
            with self.assertRaises(ValueError):
                roman_to_int_safe(i)

        for i in WRONG_ROMAN:
            with self.assertRaises(ValueError):
                roman_to_int_safe(i)


class TestFullConvertionSafe(unittest.TestCase):
    """
    Run a full convertion test:
        int -> roman -> int
    and checks that the two integers are equals.
    This test is run only on safe version.
    """

    def full_convertion_run_safe(self, upper):
        """
        Generate all possibile integers from 1 to 9999
        run test on safe (with input check) version
        """
        for i in range(1, 10000):
            roman = int_to_roman_safe(i, upper=upper)
            arabic = roman_to_int_safe(roman)
            self.assertEqual(i, arabic)


    def test_full_convertion_lower_safe(self):
        """
        Test lower case output
        """
        self.full_convertion_run_safe(False)


    def test_full_convertion_upper_safe(self):
        """
        Test upper case output
        """
        self.full_convertion_run_safe(True)


class TestFullConvertionFast(unittest.TestCase):
    """
    Run a full convertion test:
        int -> roman -> int
    and checks that the two integers are equals.
    This test is run only on fast version.
    """

    def full_convertion_run_fast(self, upper):
        """
        Generate all possibile integers from 1 to 9999
        run test on fast (without input check) version
        """
        for i in range(1, 10000):
            roman = int_to_roman(i, upper=upper)
            arabic = roman_to_int(roman)
            self.assertEqual(i, arabic)


    def test_full_convertion_lower_fast(self):
        """
        Test lower case output
        """
        self.full_convertion_run_fast(False)


    def test_full_convertion_upper_fast(self):
        """
        Test upper case output
        """
        self.full_convertion_run_fast(True)


class TestFullConvertionCombined(unittest.TestCase):
    """
    Run a full convertion test:
        int -> roman -> int
    and checks that the two integers are equals.
    This test is run on both fast and safe version
    This test ensure safe and fast version interoperability
    and consistency
    """

    def full_convertion_run(self, upper):
        """
        Generate all possibile integers from 1 to 9999
        run test on both fast and safe version.
        """
        for i in range(1, 10000):
            safe_roman = int_to_roman_safe(i, upper=upper)
            fast_roman = int_to_roman(i, upper=upper)
            self.assertEqual(safe_roman, fast_roman)

            if i % 2 == 0:
                safe_arabic = roman_to_int_safe(safe_roman)
                fast_arabic = roman_to_int(fast_roman)
            else:
                safe_arabic = roman_to_int_safe(fast_roman)
                fast_arabic = roman_to_int(safe_roman)
            
            self.assertEqual(safe_arabic, fast_arabic)
            self.assertEqual(i, fast_arabic)


    def test_full_convertion_lower_fast(self):
        """
        Test lower case output
        """
        self.full_convertion_run(False)


    def test_full_convertion_upper_fast(self):
        """
        Test upper case output
        """
        self.full_convertion_run(True)


if __name__ == "__main__":
    unittest.main()
