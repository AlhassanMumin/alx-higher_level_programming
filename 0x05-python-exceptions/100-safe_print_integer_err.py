#!/usr/bin/python3
import sys
# 100-safe_print_integer_err.py
def safe_print_integer_err(value):
    """print integers or stder

    args:
        value: the value to print

    Return: Either a true or a false
    """
    TorF = False
    try:
        print("{:d}".format(value))
        TorF = True
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return TorF
