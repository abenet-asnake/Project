# A class that is not instantiated 
# contains abstract method that be implemented  by derived classes
# abc stands for Abstract Base Classes. It is a Python module that provides tools for defining abstract classes.
# ABC stands for Abstract Base Class. It is a class from the abc module used as a base for creating abstract classes.


from abc import ABC, abstractmethod


class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(AbstractShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

#output 
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")