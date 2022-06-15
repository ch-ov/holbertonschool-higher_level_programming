#!/usr/bin/python3
"""10. And now, the Square!"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.size}"
    """end 10. And now, the Square!"""

    """11. Square size"""
    """adding the public getter and setter size"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    """end 11. Square size"""

    """12. Square update"""
    def update(self, *args, **kwargs):
        """assigns following attributes"""
        if args is not None and len(args) > 0:
            attr = ["id", "size", "x", "y"]
            for x in range(len(args)):
                setattr(self, attr[x], args[x])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    """end 12. Square update"""

    """14. Square instance to dictionary representation"""
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_square = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dict_square
    """end 14. Square instance to dictionary representation"""
