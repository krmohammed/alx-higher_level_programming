#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx not in range(len(my_list)):
        return my_list
    del my_list[idx]
    return my_list
