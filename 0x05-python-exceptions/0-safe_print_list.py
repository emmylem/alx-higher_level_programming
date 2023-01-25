#!/usr/bin/python3
"""Prints elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list."""
    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num = num + 1
        except IndexError:
            break
    print("")
    return (num)
