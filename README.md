# roman_numbers [![Build Status](https://travis-ci.com/FilippoRanza/roman_numbers.svg?branch=master)](https://travis-ci.com/FilippoRanza/roman_numbers) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/1d68e4e50fb44ace853305e19e46b8ae)](https://app.codacy.com/app/FilippoRanza/roman_numbers?utm_source=github.com&utm_medium=referral&utm_content=FilippoRanza/roman_numbers&utm_campaign=Badge_Grade_Dashboard)
Convert integers to roman numerals and vice versa

## Description
roman_numbers is a simple Python library that lets you convert from python int to 
roman numerals (represented as a python string) or convert from roman numerals 
to python int. 

## Installation
There's no installation method available at this moment.

## Usage
Once installed you can simply import this module
in the usual way. For a complete function
documentation refer to pydoc.

## Notes
### Large Numbers
No system to write large roman numeral is currently supported.

### Safe Version
Convetion functions are available in two different forms:
  + safe: those versions(function name end with _safe) perform 
  checks on the input, ensuring that input type is correct and 
  input variables are in the right form.

  + fast: those versions don't perform any check on the input, 
  assuming the values are both of the correct type and in the 
  correct form.

### Correct Input Format
  + int_to_roman (integer to roman numeral convertion) consider 
  as correct input any python integer lerger then zero

  + roman_to_int (roman numeral to integer convertion) consider
  as correct input ant python string that contains a correct 
  roman numeral and nothing more. To test if a string is correct
  or not is_valid_roman function is available




