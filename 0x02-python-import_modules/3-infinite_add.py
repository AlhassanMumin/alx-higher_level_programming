#!/bin/python3
if __name__ == "__main__":
    """add the argument"""
    import sys
    
    result = 0
    for ind, arg in enumerate(sys.argv):
        if ind >= 1:
            result += int(arg)
    print("{}".format(result))
