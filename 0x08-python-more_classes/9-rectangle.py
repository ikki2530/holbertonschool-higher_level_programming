#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ initialize the objects

        Arguments:
            width {int} -- width of the rectangle
            height {int} -- height of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get the width

        Returns:
            int -- Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectangle

        Arguments:
            value {int} -- new value of the width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height

        Returns:
            int -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle

        Arguments:
            value {int} -- new value of the height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle

        Returns:
            [int] -- the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter

        Returns:
            int -- perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """use to fill a rectangle

        Returns:
            string -- square of #
        """
        rectang = ""
        if self.width == 0 or self.height == 0:
            return rectang
        else:
            for i in range(self.height):
                rectang += str(self.print_symbol) * self.__width
                if i != (self.height - 1):
                    rectang += "\n"
            return rectang

    def __repr__(self):
        """return an string

        Returns:
            string -- Rectangle(width, height)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare areas of two rectangles

        Arguments:
            rect_1 {Rectangle} -- rectangle 1
            rect_2 {Retangle} -- rectangle 2

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle

        Returns:
            Rectangle -- object rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Print a square

        Keyword Arguments:
            size {int} -- size of the square (default: {0})

        Returns:
            int -- object of type square
        """
        return Rectangle(size, size)
