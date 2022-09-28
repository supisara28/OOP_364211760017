"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

class Labtop:
    my_labtop = []

    def __init__(self, brand, model, cpu, ram, display, storage, price):
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price
        self.my_labtop.append(self)

    def display_labtop(self):
        print(f'Brand:{self.__brand} '
              f'Model:{self.__model} '
              f'CPU:{self.__cpu} '
              f'RAM:{self.__ram} '
              f'Display:{self.__display} '
              f'Storage:{self.__storage} '
              f'Price:{self.__price} ')
    def get_brand(self):
        return self.__brand
    def set_brand(self,__brand):
        self.__brand = __brand
    def get_model(self):
        return self.__model
    def set_model(self,__model):
        self.__model = __model
    def get_cpu(self):
        return self.__cpu
    def set_cpu(self,__cpu):
        self.__cpu = __cpu
    def get_ram(self):
        return self.__ram
    def set_ram(self,__ram):
        self.__ram = __ram
    def get_display(self):
        return self.__display
    def set_display(self,__display):
        self.__display = __display
    def get_storage(self):
        return self.__storage
    def set_storage(self,__storage):
        self.__storage = __storage
    def get_price(self):
        return self.__price
    def set_price(self,__price):
        self.__price = __price