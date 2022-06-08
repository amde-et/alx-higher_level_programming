#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(roman_string)):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i - 1]]:
            integer += roman[roman_string[i]] - 2 * roman[roman_string[i - 1]]
        else:
            integer += roman[roman_string[i]]
    return (integer)
