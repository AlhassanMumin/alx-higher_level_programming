#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    """print the resulst of 2 integers

    args:
        a: the divident
        b: the divisor

    Return: the quotient
    """
    result = 0

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
