#Defining the student class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# method to display student information
    def display_info(self) :
        print(f"student Name: {self.name}, Age: {self.age}")

#creating a student oject and displaying information
student1 = Student("Richard Dok", 3.3) 
student2 = Student("Victoria", 2.9)

student1.display_info()
student2.display_info()
