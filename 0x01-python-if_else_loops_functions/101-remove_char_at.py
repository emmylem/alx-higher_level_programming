#!/usr/bin/python3
def remove_char_at(str, n):
    # creates copy of string
    if (n < 0):
        return (str)
    return (str[:n] + str[n + 1:])
