#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = 0
    denum = 0
    for i, k in my_list:
        num += i * k
        denum += k
    return num / denum
