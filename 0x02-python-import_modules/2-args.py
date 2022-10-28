#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    """this function prints arguments"""
    import sys

    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for ind in range(len(sys.argv)):
        if ind >= 1:
            print("{:d}: {}".format(ind, sys.argv[ind]))
