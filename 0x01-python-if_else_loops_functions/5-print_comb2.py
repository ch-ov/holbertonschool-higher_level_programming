#!/usr/bin/python3
for y in range(0, 100):
    if y == 99:
        print(y)
    if y < 10:
        print(f"0{y}, ", end="")
    elif y >= 10:
        print(f"{y}, ", end="")
