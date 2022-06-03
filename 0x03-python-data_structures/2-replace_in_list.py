#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for x in my_list:
        if idx == my_list.index(x):
            my_list.pop(idx)
            my_list.insert(idx, element)
            return (my_list)
        elif idx >= len(my_list):
            return (my_list)
        elif idx < 0:
            return (my_list)
