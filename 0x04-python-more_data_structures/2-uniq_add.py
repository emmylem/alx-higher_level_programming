#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer)"""
    total = 0
    for x in set(my_list):
        total += x
    return (total)
