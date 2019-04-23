#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

"""
integer_to_roman - convert from Python integer
to a Roman Numeral (Python string)
"""


UPPER_UNITS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
UPPER_TENS = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C']
UPPER_HUNDREDS = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
UPPER_CONVERT = [UPPER_HUNDREDS, UPPER_TENS, UPPER_UNITS]


LOWER_UNITS = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
LOWER_TENS = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc', 'c']
LOWER_HUNDREDS = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm', 'm']
LOWER_CONVERT = [LOWER_HUNDREDS, LOWER_TENS, LOWER_UNITS]

def int_to_roman(number, upper=True):
    """
    Convert give integer into
    equivalent Roman Numeral(python string)

    number: integer to convert
    upper: if True return an upper case Roman Numeral,
           otherwise a lower case Numeral is returned

    return: Roman Numeral Equivalent to input number
    """

    out = ''

    out += 'M' * (number // 1000)
    number %= 1000

    reduce = 100
    convert = UPPER_CONVERT if upper else LOWER_CONVERT

    for conv in convert:
        out += conv[number // reduce]
        number %= reduce
        reduce //= 10

    return out


def int_to_roman_safe(number, upper=True):
    """
    Convert give integer into
    equivalent Roman Numeral(python string),
    this version perform security and type
    check on the input arguments:
        raises ValueError if number is not
        int

        raises ValueError if upper is not
        bool

        raises ValueError if number <= 0


    number: integer to convert
    upper: if True return an upper case Roman Numeral,
           otherwise a lower case Numeral is returned

    return: Roman Numeral Equivalent to input number
    """

    if not isinstance(number, int):
        raise ValueError(int)

    if not isinstance(upper, bool):
        raise ValueError(bool)

    if number <= 0:
        raise ValueError('input must be larger then 0')

    return int_to_roman(number, upper)
