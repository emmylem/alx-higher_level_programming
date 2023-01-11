#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # a function that replaces all occurrences
    new_list = my_list[:]
    for x in range(len(new_list)):
        if (new_list == search):
            new_list[i] = replace
    return (new_list)
