#!/usr/bin/python3
#100-my_calculator.py
if __name__=="__main__":
    """It handles basic operations"""
    import sys
    from calculator_1 import add, sub, mul, div

    
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    first = int(sys.argv[1])
    second = int(sys.argv[3])
    
    add = add(first, second)
    sub = sub(first, second)
    mul = mul(first, second)
    div = div(first, second)
    
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
