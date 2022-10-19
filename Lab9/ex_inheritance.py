"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

# Class Relations - Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'Name: {self.name} Age: {self.age}')

class Student(Person):
    def __init__(self, name, age, major, gpa):
        # 1
        Person.__init__(self, name, age)
        # 2
        #super.__init__(name, age)
        self.major = major
        self.gpa = gpa
    def student_info(self):
        self.person_info()
        print(f'Major: {self.major} GPA: {self.gpa}')

# create object
p1 = Person("Supisara", 22)
s1 = Student("Jeno", 22, "MIT",3.50)

p1.person_info()
s1.person_info()

s1.student_info()
