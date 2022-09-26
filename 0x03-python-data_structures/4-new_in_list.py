#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace an element at a position"""

    list_range = len(my_list)
    if idx < 0 or idx >= list_range:
        return my_list
    new_list = []
    for ind in range(list_range):
        if ind == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[ind])
    return new_list
