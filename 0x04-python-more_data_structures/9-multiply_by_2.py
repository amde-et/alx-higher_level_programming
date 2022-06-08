#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    New_dic = {}
    for i in a_dictionary:
        Newvalue = (a_dictionary.get(i)) * 2
        New_dic.update({i: Newvalue})
    return (New_dic)
