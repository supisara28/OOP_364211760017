"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

class Labtop:
    def __init__(self, brand, model, cpu, ram, display, storage, price):
        self.__brand = brand  # private member
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price
    # getter and setter
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand

    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model = model

    def get_cpu(self):
        return self.__cpu
    def set_cpu(self,cpu):
        self.__cpu = cpu

    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram

    def get_display(self):
        return self.__display
    def set_display(self,display):
        self.__display = display

    def get_storage(self):
        return self.__storage
    def set_storage(self,storage):
        self.__storage = storage

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def __str__(self):
        print(f'Brand: {self.__brand} '
              f'Model: {self.__model} CPU: {self.__cpu} '
              f'RAM: {self.__ram} Display: {self.__display} '
              f'Storage: {self.__storage} Price: {self.__price}')

l = Labtop ("ASUS", "Vivbook 15x", "Intel Core i5-12500H", "8" ,"15.6", "512", "27990")
l.__str__()

print(l.get_brand())
l.set_brand("Lenovo")
print(l.get_brand())

print(l.get_model())
l.set_model("ideaPad Gaming3")
print(l.get_model())
l.__str__()