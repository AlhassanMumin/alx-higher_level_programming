#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """print integer values

    args:
        value: the value passed in

   Return: true or  false
   """
    TorF = False
    try:
        print("{:d}".format(value))
        TorF = True
    except (ValueError, TypeError):
        print
    return TorF
