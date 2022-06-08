#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiation with size"""
    def __init__(self, size):
        super().__init__(size, size)
