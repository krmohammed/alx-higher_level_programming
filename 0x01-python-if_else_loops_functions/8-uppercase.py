#!/usr/bin/python3
def uppercase(str):
    str_upper = ''
    for i in str:
        if ord(i) in range(97, 123):
            str_upper += chr(ord(i) - 32)
        else:
            str_upper += i
    print('{}'.format(str_upper))
