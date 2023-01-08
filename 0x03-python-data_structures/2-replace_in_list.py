#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # to replace elememts in list
    x = my_list[idx] = element
    if (idx >= 0 and idx < len(my_list)):
        return (x)
    return (my_list)
