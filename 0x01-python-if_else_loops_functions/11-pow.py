#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b < 0:
        for i in range(-b):
            res *= a
        return (1 / res)
    elif b == 0:
        return (1)
    else:
        for i in range(b):
            res *= a
        return (res)
