#!/usr/bin/python3
""" class Rectangle that defines a rectangle by: (based on 4-rectangle.py) """


class Rectangle:
    """ Detect instance deletion """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return int(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return int(2 * (self.width + self.height))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return('')
        else:
            return((('#' * self.width) + '\n') *
                   (self.height - 1) + '#' * self.width)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")