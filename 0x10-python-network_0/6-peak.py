#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    '''finds peak'''
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
