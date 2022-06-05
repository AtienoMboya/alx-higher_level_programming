#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1)
    for idx in range(len(my_list)-1):
        print("{:d}".format(my_list[idx]))
        idx--
    if idx < 0:
        break
