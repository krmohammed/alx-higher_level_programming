#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string is not None:
        r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,\
                'C': 100, 'D': 500, 'M': 1000}
        value = 0
        for i in range(len(roman_string)):
            if i < len(roman_string) - 1:
                if r_dict[roman_string[i]] < r_dict[roman_string[i + 1]]:
                    value -= r_dict[roman_string[i]]
                else:
                    value += r_dict[roman_string[i]]
            else:
                value += r_dict[roman_string[i]]
    else:
        return 0
