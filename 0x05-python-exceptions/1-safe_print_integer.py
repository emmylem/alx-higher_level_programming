#!/usr/bin/python3
"""Prints an integer."""


def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
    value (int): The integer to print."""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
