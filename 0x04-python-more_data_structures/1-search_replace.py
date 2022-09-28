#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """search and replace an element"""

    new_list = []
    for indx in my_list:
        if indx == search:
            new_list.append(replace)
        else:
            new_list.append(indx)

    return new_list
