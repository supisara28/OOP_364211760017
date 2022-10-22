"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

class Person:
    def __init__(self, name, age, weigh, height):
        self.__name = name
        self.__age = age
        self.__weigh = weigh
        self.__height = height
    def __str__(self):
        print(f'Name : {self.__name}'
              f'Age : {self.__age} '
              f'Weigh : {self.__weigh} '
              f'Height : {self.__height}')
    # getter and setter
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def get_weigh(self):
        return self.__weigh
    def set_weigh(self,weigh):
        self.__weigh = weigh
    def get_height(self):
        return self.__height
    def set_height(self,height):
        self.__height = height

class Student(Person):
    def __init__(self,name,age,weigh,height,major):
        super().__init__(name,age,weigh,height)
        self.__major = major
    def __str__(self):
        super().__str__()
        print(f'Major: {self.__major}')

class Vaccine:
    all_vaccine = ["Sinovac", "Astazeneca","Moderna","Pfizer","Sinnopharm"]

    def __init__(self,vac_name):
        self.__vac_name = vac_name
    def vaccine_info(self):
        print(f'vaccine name: {self.__vac_name}')
    def get_name(self):
        return self.__vac_name
    def get_all_vaccine(self):
        for x in self.all_vaccine:
            print(x)

class Vaccine_Passport:

    def __init__(self,owner):
        self.owner = owner
        self.vaccinated = list()
        self.date = list()
    def add_vaccine(self, Vaccine):
        self.vaccinated.append(Vaccine)
    def add_date(self,date):
        self.date.append(date)
    def vaccine_passport_info(self):
        print(f'MI Vaccinated Passport: ')
        self.owner.__str__()
        c = 1
        if len(self.vaccinated) == 0:
            print(f'\t No vaccinated data.')
        else:
            #for x in self.vaccinated:
                #print(f'{c}.{x.get_name()}')
                #c += 1
            for x in range(len(self.vaccinated)):
                print(f'{c}. {self.vaccinated[x].get_name()} '
                            f'date: {self.date[x]}')
                c += 1
