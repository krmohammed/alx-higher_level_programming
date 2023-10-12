#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = None
        key = None
        for i, j in a_dictionary.items():
            if best is None or j > best:
                best = j
                key = i
        return key
    else:
        return None
