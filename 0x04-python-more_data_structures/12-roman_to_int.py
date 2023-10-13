#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        r_dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        roman_int = 0
        for i in range(len(roman_string)):
            if i < (len(roman_string) - 1):
                if r_dict[roman_string[i]] < r_dict[roman_string[i + 1]]:
                    roman_int -= r_dict[roman_string[i]]
                else:
                    roman_int += r_dict[roman_string[i]]
            else:
                roman_int += r_dict[roman_string[i]]
        return roman_int
    else:
        return 0
