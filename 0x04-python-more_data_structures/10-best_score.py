#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    if a_dictionary:
        maxn = max(list(a_dictionary.values()))
        for k, v in a_dictionary.items():
            if v == maxn:
                key = k
    return key
