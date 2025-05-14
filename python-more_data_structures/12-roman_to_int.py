#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    new_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    longeur = len(roman_string)
    for i in range(longeur):
        if (i + 1 < longeur and
                new_dict[roman_string[i]] < new_dict[roman_string[i + 1]]):
            total -= new_dict[roman_string[i]]
        else:
            total += new_dict[roman_string[i]]
    return total
