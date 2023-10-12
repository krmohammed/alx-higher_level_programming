#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    denum = 0
    for i, k in my_list:
        num += i * k
        denum += k
    return num / denum
