#!/usr/bin/python3

def multiple_returns(sentence):
    slist = []
    slist[:0] = sentence
    if len(slist) == 0:
        slist[0] = None
    tup = (len(slist), slist[0])
    return tup
