#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for llave in sorted(a_dictionary):
        print("{}: {}".format(llave, a_dictionary[llave]))
