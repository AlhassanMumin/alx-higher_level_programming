#!/usr/bin/python3
def remove_char_at(str, n):
    cop = ''
    for char in str:
        if str.index(char) == n:
            continue
        cop += char
    return (cop)
