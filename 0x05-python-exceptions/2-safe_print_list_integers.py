#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_len = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            int_len += 1
        except:
            continue
    print()
    return int_len
