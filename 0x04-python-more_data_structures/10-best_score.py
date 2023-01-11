#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer"""
    if (not isinstance(a_dictionary, dict) or len(a_dictionary) == 0):
        return (None)

    ret = list(a_dictionary.keys())[0]
    wow = a_dictionary[ret]
    for x, y in a_dictionary.items():
        if (y > wow):
            wow = y
            ret = x
    return (ret)
