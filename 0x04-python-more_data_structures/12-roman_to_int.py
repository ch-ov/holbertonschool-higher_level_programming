#!/usr/bin/python3
def roman_to_int(roman_string):

    roman = {}
    roman['I'] = 1
    roman['V'] = 5
    roman['X'] = 10
    roman['L'] = 50
    roman['C'] = 100
    roman['D'] = 500
    roman['M'] = 1000
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0

    for i, c in enumerate(roman_string):
        if (i+1) == len(roman_string) or roman[c] >= roman[roman_string[i+1]]:
            result += roman[c]
        else:
            result -= roman[c]
    return result
