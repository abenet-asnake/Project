"""
this is the fisrt class 

class 
 class is a blue printing of objects , it defines filed which is (variable) and methods (functions)

 object 
    an instance of classes and represent a spesfic entity in the real world 

"""

class Student:
    # constructor that initilizes 
    # self is an instance of the class it allows you to access the attributies  and methods 
    #instance is 
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}, Age:{self.age}")


#creating an object 
student1=Student("Abenet",32)
student1.display()