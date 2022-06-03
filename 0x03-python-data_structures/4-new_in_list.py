#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    for x in my_list:
        if idx == my_list.index(x):
            copy[idx] = element
            return (copy)
        elif idx >= len(my_list):
            return (copy)
        elif idx < 0:
            return (copy)
