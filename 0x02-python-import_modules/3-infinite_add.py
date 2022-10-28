#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    """add the argument"""
    import sys

    result = 0
    for ind in range(1, len(sys.argv)):
        result += int(sys.argv[ind])    
    print("{}".format(result))
