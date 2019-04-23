#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

"""
roman_numbers install script
"""

import setuptools

with open('README.md') as file:
    LONG_DESCRIPTION = file.read()


setuptools.setup(
    name="roman_numbers",
    version="0.0.1",
    author="Filippo Ranza",
    author_email="filipporanza@gmail.com",
    description="convert arabic integer to roman numeral and vice versa",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/FilippoRanza/roman_numbers",
    packages=setuptools.find_packages(),
)
