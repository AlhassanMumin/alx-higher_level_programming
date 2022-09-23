#!/usr/bin/python3
for first in range(0, 9, 1):
    for second in range(1, 10, 1):
        if not second <= first:
            if first < 8:
                print("{}{}".format(first, second), end=", ")
print("{}{}".format(first, second))
