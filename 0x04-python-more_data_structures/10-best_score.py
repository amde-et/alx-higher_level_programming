#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        v = list(a_dictionary.values())
        k = list(a_dictionary.keys())
        return (k[v.index(max(v))])
