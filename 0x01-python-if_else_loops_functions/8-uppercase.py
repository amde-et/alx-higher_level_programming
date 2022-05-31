#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{:s}".format(char), end="")
    print('')
