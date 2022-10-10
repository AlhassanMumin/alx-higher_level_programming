#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """divide element by element

    args:
        my_list_1: the divident
        my_list_2: the divisor
        list_length: the length of the list to divide

    Return: the result in a new list
    """
    new_list = []

    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            div = 0
            print("out of range")
        except (TypeError, ValueError):
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 9")
        finally:
            new_list.append(div)
    return new_list
