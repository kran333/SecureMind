class Rectangle:
    def __init__(self, x, y, w, h):
        if w < 0 or h < 0:
            raise ValueError("Width and height should be positive")
        self.__x = x
        self.__y = y
        self.__width = w
        self.__height = h
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    def __str__(self):
        return f"Rectangle[x={self.__x}, y={self.__y}, width={self.__width}, height={self.__height}]"


rect_obj = Rectangle(20, -10, 20, 30)
print(rect_obj)