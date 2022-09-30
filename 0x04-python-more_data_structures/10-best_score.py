#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    """search and return the best score"""

    if a_dictionary == None:
        return None

    biggest_val = list(a_dictionary.keys())[0]

    for key, val in a_dictionary.items():
        if val > a_dictionary.get(biggest_val):
            biggest_val = key
    return biggest_val 
