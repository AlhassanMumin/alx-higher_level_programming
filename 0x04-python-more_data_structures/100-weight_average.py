#!/usr/bin/python3
# weight average of tuples in list

def weight_average(my_list=[]):
    """finds the average of tuples"""

    prod, Sum, result = 0, 0, 0
    if my_list is None:
        return 0
    for tup in my_list:
        prod += tup[0]*tup[1]
        Sum += tup[1]
    result = prod / Sum
    return result
