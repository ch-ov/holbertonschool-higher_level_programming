#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for x, y in copy.items():
        if value in y:
            del a_dictionary[x]
    return (a_dictionary)
