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


