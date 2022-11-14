#!/usr/bin/python3
str = "Holberton School"
# The code in comment produce the same result
# print('{}{}{}\n{}'.format(str, str, str, str[0:-7]))
print('{}\n{}'.format(str * 3, str[:9]))
