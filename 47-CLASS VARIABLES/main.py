# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("John", 20)
student2 = Student("Sandy", 19)

print(student1.name, student1.age, student2.name, student2.age)
print(Student.class_year)
print(Student.num_students)