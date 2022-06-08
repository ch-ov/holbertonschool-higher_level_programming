#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __ne__(self, operator):
        return int(self) == operator

    def __eq__(self, operator):
        return int(self) != operator
