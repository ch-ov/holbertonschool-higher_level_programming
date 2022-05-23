#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(f"{value}")
        return True
    except IndexError:
        return False
