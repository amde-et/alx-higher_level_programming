#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
        return (a_dictionary)
    except KeyError:
        return (a_dictionary)
