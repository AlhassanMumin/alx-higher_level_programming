#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
stri = "Last digit of {} is {} {}"
if number >= 0:
    last_dig = number % 10
    if last_dig > 5:
        print(stri.format(number, last_dig, "and is greater than 5"))
    elif last_dig == 0:
        print(stri.format(number, last_dig, "and is 0"))
    else:
        print(stri.format(number, last_dig, "and is less than 6 and not 0"))
else:
    num1 = number*-1
    stri = "Last digit of {} is -{} {}"
    last_dig = num1 % 10
    print(stri.format(number, last_dig, "and is less than 6 and not 0"))
