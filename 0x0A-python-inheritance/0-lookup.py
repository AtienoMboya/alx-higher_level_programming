#!/usr/bin/python3

def lookup(obj):
    """function to return list of available attributes and methods of an object

    Args:
        obj: the object
    """
    return dir(obj)
