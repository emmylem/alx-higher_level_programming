#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    [print("{}: {}".format(f, a_dictionary[f])) for f in sorted(a_dictionary)]
