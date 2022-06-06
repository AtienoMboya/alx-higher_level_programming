#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = my_list[:]
    for idx in range(len(new)-1):
        if new[idx] % 2 == 0:
            new[idx] = True
        else:
            new[idx] = False

    return (new)
