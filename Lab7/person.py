"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

class Person:
    def __init__(self, name, age):
        self._name = name  # protected member
        self._age = age  # protected member
    def __str__(self):
        print(f'Name: {self._name} Age: {self._age}')

class Student(Person):
    def __init__(self, name, age, major,):
        self.major = major  # public member
        Person.__init__(self, name, age)
    def __str__(self):
        print(f'Name: {self._name} Age: {self._age}  Major: {self.major}')

#  object Person
p = Person("Supisara",21)
p.__str__()

p._name = "JENO"
p.__str__()

#  object Student
s = Student("JAEMIN", 22, "MIT")
s.__str__()

s._name = "JISONG"
s.__str__()