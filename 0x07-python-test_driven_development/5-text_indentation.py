#!/usr/bin/python3
""" Text indentation """


def text_indentation(text):
    """ Prints with 2 lines after each of these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    if len(text) == 0:
        return
    tmp = text[0]
    chars = ['.', '?', ':']
    for char in text:
        if char == ' ' and tmp in chars:
            continue
        tmp = char
        print(char, end='')
        if char in chars:
            print()
            print()
