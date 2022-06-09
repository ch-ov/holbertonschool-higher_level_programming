#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the \
    Pascal’s triangle of n"""
    list = []
    if n <= 0:
        return list
    for a in range(1, n+1):
        tmp = []
        for b in range(0, a):
            tmp.append(1)
        list.append(tmp)

    for c in range(1, n):
        for d in range(c, 0, -1):
            list[c][d - 1] = list[c - 1][d - 2] + list[c - 1][d - 1]
            list[c][c] = 1
            list[c][0] = 1
    return list