#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    Newdict = a_dictionary.copy()
    try:
        for key in Newdict:
            if value == a_dictionary[key]:
                del a_dictionary[key]
        return (a_dictionary)
    except KeyError:
        return (a_dictionary)
