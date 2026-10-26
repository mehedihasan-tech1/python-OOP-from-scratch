"""Class Variable"""


class Student:

    grad_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name,
        self.age = age,
        Student.num_students += 1


student1 = Student("Mehedi", 30)
student2 = Student("Hasan", 34)
student3 = Student("Shuvo", 35)

print(Student.num_students)
print(student1.name)
print(student1.age)
print(Student.grad_year)
