#!/usr/bin/python3
def magic_string():
    magic_string.num_iter = getattr(magic_string, "num_iter", 0) + 1
    return "BestSchool, "*(magic_string.num_iter - 1) + "BestSchool"
