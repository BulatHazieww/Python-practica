
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return math.isclose(self.area(), other.area())

    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() < other.area()

    def __gt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() > other.area()


class Circle(Shape):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def info(self):
        print("Название фигуры:", self)
        print("Радиус:", self.radius)
        print("Площадь:", round(self.area(), 2))


class Rectangle(Shape):

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Стороны должны быть положительными")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def info(self):
        print("Название фигуры:", self)
        print("Ширина:", self.width)
        print("Высота:", self.height)
        print("Площадь:", round(self.area(), 2))


circle = Circle(5)
rectangle = Rectangle(6, 4)

print("=== ИНФОРМАЦИЯ О КРУГЕ ===")
circle.info()

print("\n=== ИНФОРМАЦИЯ О ПРЯМОУГОЛЬНИКЕ ===")
rectangle.info()

print("\n=== СРАВНЕНИЕ ФИГУР ===")

if circle > rectangle:
    print("Площадь круга больше площади прямоугольника")
elif circle < rectangle:
    print("Площадь круга меньше площади прямоугольника")
else:
    print("Площади фигур равны")
