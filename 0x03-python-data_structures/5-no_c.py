#!/usr/bin/python3

def no_c(my_string):
    string_ls = []
    string_ls[:0] = my_string
    for element in string_ls:
        if element == 'c' or element == 'C':
            string_ls.remove(element)
    my_string = ''.join([str(item) for item in string_ls])
    return my_string
