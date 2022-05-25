#  * OS-2, 2022
# Written by: Daniel Khasin and Nadav Imergreen
# ID: 316558766 & 307942581
# Login: danielkh & nadavyi
#
# ======================================================================
# File ex3.py:
# This program defines classes of a varied shapes with specific methods using inheritance and polymorphism.
#
# ======================================================================

import math

class Shape(object):

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius
        if radius < 0:
            self.__radius = 1

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius
        if radius < 0:
            self.__radius = 1

    def area(self):
        return "area = " + str((self.__radius ** 2) * math.pi)

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return 'Circle: radius = ' + str(self.__radius)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__height = height
        if height < 0:
            self.__height = 1
        self.__width = width
        if width < 0:
            self.__width = 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        if width < 0:
            self.__width = 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__width = height
        if height < 0:
            self.__height = 1

    def area(self):
        return "area = " + str(self.__height * self.__width)

    def perimeter(self):
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        return 'Rectangle: width = ' + str(self.__width) + ', height = ' + str(self.__height)


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

    def __str__(self):
        return 'Square: length = ' + str(self.height)


"""==========================================================================================="""


class ShapesCollection(object):
    def __init__(self, shapes):
        self.__shapes = shapes

    def __len__(self):
        return len(self.__shapes)

    def insert(self, s):
        if isinstance(s, Shape):  # check new object to be in type Shape
            if self.__len__() == 0: # case the list is empty
                self.__shapes.insert(0, s)
                return

            for i in range(self.__len__()):  # insert the new object to the list in order
                if s <= self.__shapes[i]:
                    self.__shapes.insert(i, s)
                    break
                elif i == self.__len__() - 1: # case new obj is the biggest
                    self.__shapes.insert(i + 1, s)


    def __str__(self):
        str = "collection in Shapes: \n"
        for i in self.__shapes:
            str += i.__str__() + '\n'
        return str

    def biggestPerimeterDiff(self):
        return "biggest perimeter diff = " + str(self.__shapes[self.__len__() - 1].perimeter() - self.__shapes[0].perimeter())

    def howManyQuadrilaterals(self):
        num_of_quadrilaterals = 0
        for i in self.__shapes:
            if isinstance(i, Square) or isinstance(i, Rectangle):
                num_of_quadrilaterals += 1
        return "howManyQuadrilaterals = " + str(num_of_quadrilaterals)

    def sameAreaAs(self, s):
        lst = []
        for i in self.__shapes:
            if i == s:
                lst.append(i)
        return lst


"""==========================================================================================="""
# if __name__ == "__main__":
#     c0 = Rectangle(4, 6)
#     c1 = Square(6)
#     c2 = Circle(5)
#     lst = [c1, c2]
#     sc = ShapesCollection(lst)
#     print(sc.__str__())
#     sc.insert(c0)
#     print(sc.__str__())
#
#     print (c0.area())
#     print (c1.area())
#     print (c2.area())
#     print (c2.perimeter())
#     print (c0.perimeter())
#     print (c1.perimeter())
#     print (sc.biggestPerimeterDiff())
#     print (sc.howManyQuadrilaterals())
#
#     same_area_lst = sc.sameAreaAs(c1)
#     for i in same_area_lst:
#         print (i)

