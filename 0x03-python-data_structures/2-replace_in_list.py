#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_range = len(my_list)
    if idx < 0 or idx >= list_range:
        return my_list
    my_list[idx] = element
    return my_list
