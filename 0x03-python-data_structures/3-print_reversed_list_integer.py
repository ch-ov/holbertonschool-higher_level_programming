#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for x in range(len(my_list)):
            print(f"{my_list[-x -1]}")
