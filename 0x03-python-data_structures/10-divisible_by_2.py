#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            div.append(True)
        else:
            div.append(False)
    return (div)
