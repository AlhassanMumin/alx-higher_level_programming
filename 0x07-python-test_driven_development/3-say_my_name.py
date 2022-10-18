#!/usr/bin/python3
# 3-say_my_name.py
"""defines a say name function"""

def say_my_name(first_name, last_name=""):
    """It will print a string parsed in as a name
    Only strings are expected to be parsed

    raises:
        TypeError: when first name is not parsed
    raises:
        TypeError: if the argument parsed are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
