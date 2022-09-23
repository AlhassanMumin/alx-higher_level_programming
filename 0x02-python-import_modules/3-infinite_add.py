#!/bin/python3
if __name__ == "__main__":
    """add the argument"""
    import sys
    
    result = 0
    for ind in range(len(sys.argv)):
        if ind >= 1:
            result += int(sys.argv[ind])
    print("{}".format(result))
