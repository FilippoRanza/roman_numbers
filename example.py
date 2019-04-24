#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

"""
example.py - An simple script show
roman_numbers usage:
convert given number from command line or stdin
from arabic to roman or from roman to arabic.

When run with command line arguments convets them,
otherwise converts from stdin. To stop convertion
from stdin input an empty line or EOF
"""

import re
from sys import argv

import roman_numbers

NUMBER = re.compile(r'\d+')


def readline():
    """
    read lines from stdin
    until an empty line or EOF
    is reached
    """
    while True:
        try:
            line = input()
            if line:
                yield line
            else:
                break
        except EOFError:
            break


def string_convert(string):
    """
    Finds if given string string is
    a roman number,  an arabic number
    or something else.
    If string is a roman number returns its convertion
    into an integer.
    If string is an arabic number returns its convertion
    into a roman numeral.
    Otherwise returns None.
    """
    out = None
    # check that given string is a roman numeral
    if roman_numbers.is_valid_roman(string):
        # uses fast version, without checks, because string is correct
        out = roman_numbers.roman_to_int(string)

    # check that given string is an arabic number
    elif NUMBER.fullmatch(string):
        # converts it into an integer
        tmp = int(string)
        if tmp:
            # convert the integer into a roman numeral, if it's not zero
            out = roman_numbers.int_to_roman(tmp)

    return out


def line_convert():
    """
    Converts input from stdin
    """
    for line in readline():
        conv = string_convert(line)
        if conv:
            print(conv)


def args_convert(args):
    """
    Convet input from command line
    """
    for arg in args:
        conv = string_convert(arg)
        if conv:
            print(arg, '=', conv)


def main():
    """
    If command line arguments
    are available converts them
    otherwise converts from stdin
    """
    args = argv[1:]
    if args:
        args_convert(args)
    else:
        line_convert()


if __name__ == "__main__":
    main()
