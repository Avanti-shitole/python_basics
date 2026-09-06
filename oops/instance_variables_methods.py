class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Avanti", 22)
student2 = Student("Rahul", 23)

student1.display()
student2.display()