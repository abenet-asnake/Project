"""

Polymorphism in Python means having many forms. 
It allows objects of different classes to be treated as objects of a common superclass, 
mainly by using methods with the same name but different implementations.

"""


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius* self.radius
    

class Rectangle(Shape):
    def __init__(self, height,width):
        self.height=height
        self.width=width
    
    def area(self):
        return self.width *self.height
    


#list of Shapes 

shapes=[Circle(6),Rectangle(4,8)]

for shape in shapes:
    print("Area", shape.area())
