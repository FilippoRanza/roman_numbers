#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

"""
roman_to_integer - convert from
Roman Numeral(Python string) to Python integer
"""


from .check_roman_numeral import is_valid_roman


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


def roman_to_int(roman):
    """
    Convert input Roman Numeral into
    the equivalent interger(python int)

    roman: string to convert

    return: integer value of input Roman Numeral
    """

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


def roman_to_int_safe(roman):
    """
    Convert input Roman Numeral into
    the equivalent interger(python int),
    this version perform security and type
    check on the input arguments:
        raises ValueError if roman is not
        str

        raises ValueError if roman does not
        pass is_valid_roman test

    roman: string to convert

    return: integer value of input Roman Numeral
    """


    if not isinstance(roman, str):
        raise ValueError(str)

    if not is_valid_roman(roman):
        raise ValueError('Malformatted Roman Numeral')

    return roman_to_int(roman)
