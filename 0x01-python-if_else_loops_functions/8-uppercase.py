#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 95 and ord(x) <= 124:
            x = chr(ord(x) - 32)
        print(f"{x}", end="")
    print()
