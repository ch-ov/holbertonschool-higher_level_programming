#!/usr/bin/python3


from models.base import Base
"""2. First Rectangle"""

class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """end 2. First Rectangle"""

    """3. Validate attributes"""
    """validation of all setter methods and instantiation (id excluded)"""
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        """end 3. Validate attributes"""

    """4. Area first"""
    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__height * self.__width
    """end 4. Area first"""

    """5. Display #0 && 7. Display #1"""
    def display(self):
        """prints in stdout the Rectangle instance with the character #\
        by taking care of x and y"""
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)
    """end 5. Display #0 && 7. Display #1"""

    """6. __str__"""
    def __str__(self):
        """overriding the __str__ method so that it returns \
         [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"
    """end 6. __str__"""

    """8. Update #0 && 9. Update #1"""
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute\
        assigns a key/value argument to attributes"""
        if args is not None and len(args) > 0:
            attr = ["id", "width", "height", "x", "y"]
            for x in range(len(args)):
                setattr(self, attr[x], args[x])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    """end 8. Update #0 && 9. Update #1"""

    """13. Rectangle instance to dictionary representation"""
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_rectangle = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return dict_rectangle
    """end 13. Rectangle instance to dictionary representation"""
