#!/usr/bin/python3
# 1-element_at.py
def element_at(my_list, idx):
    """Retrieves elements form the list my_list"""
    list_range = len(my_list)

    if idx < 0 or idx >= list_range:
        return "None"
    return my_list[idx]
