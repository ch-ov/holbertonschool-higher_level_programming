#!/usr/bin/python3
""" Print square """


def print_square(size):
    """ Prints a square with the character #. """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif size == 0:
        return
    for row in range(1, size + 1):
        print("#" * size)
