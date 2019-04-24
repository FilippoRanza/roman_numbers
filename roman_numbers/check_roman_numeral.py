#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

"""
roman_number - convert arabic integer to roman numeral
and vice versa
"""


import re

_ROMAN_REGEX = re.compile(
    r'M*(CM)?(CD|DC{0,3}|C{0,3})?(XC|XL|LX{0,3}|X{0,3})?(IX|IV|VI{0,3}|I{0,3})?', re.I)


def is_valid_roman(roman):
    """
    Check that roman is a string
    containing a valid Roman Numeral

    roman: string to check

    return: True is roman is a value Roman Numeral string,
            False otherwise
    """
    if not isinstance(roman, str):
        return False

    tmp = _ROMAN_REGEX.fullmatch(roman)
    return tmp is not None
