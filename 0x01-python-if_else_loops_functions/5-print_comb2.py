#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x == 9 and y == 9:
            print(f"{x}{y}")
        print(f"{x}{y}, ", end="")
