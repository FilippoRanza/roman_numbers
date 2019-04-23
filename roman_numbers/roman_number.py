#! /usr/bin/python

"""
roman_number - convert arabic integer to roman numeral
and vice versa
"""


import re

ROMAN_REGEX = re.compile(
    r'M*(CM)?(CD|DC{0,3}|C{0,3})?(XC|XL|LX{0,3}|X{0,3})?(IX|IV|VI{0,3}|I{0,3})?', re.I)


ROMAN_INT_VALUE = {
    'M'  : 1000,
    'm'  : 1000,
    'D'  : 500,
    'd'  : 500,
    'C'  : 100,
    'c'  : 100,
    'L'  : 50,
    'l'  : 50,
    'X'  : 10,
    'x'  : 10,
    'V'  : 5,
    'v'  : 5,
    'I'  : 1,
    'i'  : 1,
}


UPPER_UNITS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
UPPER_TENS = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C']
UPPER_HUNDREDS = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
UPPER_CONVERT = [UPPER_HUNDREDS, UPPER_TENS, UPPER_UNITS]


LOWER_UNITS = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
LOWER_TENS = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc', 'c']
LOWER_HUNDREDS = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm', 'm']
LOWER_CONVERT = [LOWER_HUNDREDS, LOWER_TENS, LOWER_UNITS]


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

    tmp = ROMAN_REGEX.fullmatch(roman)
    return tmp is not None


def roman_to_int(roman):
    """
    Convert input Roman Numeral into
    the equivalent interger(python int)

    roman: string to convert

    return: integer value of input Roman Numeral
    """
    if not isinstance(roman, str):
        raise ValueError(str)

    if not is_valid_roman(roman):
        raise ValueError('Malformatted Roman Numeral')

    out = 0
    prev = 0
    for token in roman:
        curr = ROMAN_INT_VALUE[token]
        if curr > prev:
            out -= prev
        else:
            out += prev
        prev = curr

    if curr > prev:
        out -= prev
    else:
        out += prev

    return out


def int_to_roman(number, upper=True):
    """
    Convert give integer into
    equivalent Roman Numeral(python string)


    number: integer to convert
    upper: if True return an upper case Roman Numeral,
           otherwise a lower case Numeral is returned

    return: Roman Numeral Equivalent to input number
    """
    if not isinstance(number, int):
        raise ValueError(int)

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


if __name__ == "__main__":
    Warning('This is not a runnable script. Please use it a library')
