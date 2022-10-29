#!/usr/bin/python3
# 101-safe_function.py
"""Defines a print safely function"""
import sys


def safe_function(fct, *args):
    """print safely function definition

    Args:
        fct (function): the passed in function
        args (argument): variable argument passed

    Return:
            the returned value on success
    """
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
