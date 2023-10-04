#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return str
    str_cpy = ''
    for i in str:
        if i == str[n]:
            continue
        str_cpy += i

    return str_cpy
