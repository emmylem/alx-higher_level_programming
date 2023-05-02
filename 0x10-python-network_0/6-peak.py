#!/usr/bin/python3
"""Peak Finding Algorithm"""


def find_peak(list_of_integers):
    """Returns the Peak of Unsorted integers"""
    if list_of_integers == []:
        return None

    num = len(list_of_integers)
    if num == 1:
        return list_of_integers[0]
    elif num == 2:
        return max(list_of_integers)

    check_int = int(num / 2)
    peak = list_of_integers[check_int]
    if peak > list_of_integers[check_int + 1] \
            and peak > list_of_integers[check_int - 1]:
        return peak
    elif peak < list_of_integers[check_int - 1]:
        return find_peak(list_of_integers[:check_int])
    else:
        return find_peak(list_of_integers[check_int + 1])
