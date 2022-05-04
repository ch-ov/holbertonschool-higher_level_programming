#!/usr/bin/python3
def print_last_digit(number):
    tmp = repr(number)[-1]
    print(f"{tmp}", end="")
    return tmp
