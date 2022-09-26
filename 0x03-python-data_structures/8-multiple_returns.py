#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """reurns a tuple """
    length = len(sentence)
    if length == 0:
        tup = (0, None)
    else:
        tup = (length, sentence[0])
    return tup
