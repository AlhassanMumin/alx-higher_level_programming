#!/usr/bin/python3
# delete some values

def complex_delete(a_dictionary, value):
    """a func to delete a key value pair
    a_dictionary - the dictionary
    arg:
        value the value to delete
    """
    while value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if val is value:
                del a_dictionary[key]
                break
    return a_dictionary 


