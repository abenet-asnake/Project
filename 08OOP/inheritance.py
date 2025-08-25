"""
Inheritance Example
"""

class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}, Age:{self.age}")


class Student (Person):
    # Student inherits a person 
    def __init__(self, name, age,studentID):
        super().__init__(name, age)
        self.studentID=studentID
    
    def show_student(self):
        print(f"Student ID={self.studentID}")


# it Ceareting an object 

student1=Student("Abenet",32,"FIS\1234")

# it shows or print out inherted method 
student1.display()

# it shows the child method including the person and the data 
student1.show_student()