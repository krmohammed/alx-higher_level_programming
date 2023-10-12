#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_be_deleted = []
    for i, j in a_dictionary.items():
        if value == j:
            to_be_deleted.append(i)
    for i in to_be_deleted:
        a_dictionary.pop(i)
    return a_dictionary
