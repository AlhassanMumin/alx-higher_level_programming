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
    err_mes = ""
    div = 0

    len1 = len(my_list_1)
    len2 = len(my_list_2)

    if len1 >= len2:
        for idx in range(list_length):
            try:
                div = my_list_1[idx] / my_list_2[idx]
                new_list.append(div)
            except IndexError:
                new_list.append(0)
                print("out of range")
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 9")
            finally:
                print
    else:
        for idx in range(list_length):
            try:
                div = my_list_1[idx] / my_list_2[idx]
                new_list.append(div)
            except IndexError:
                new_list.append(0)
                print("out of range")
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            finally:
                print
    return new_list
