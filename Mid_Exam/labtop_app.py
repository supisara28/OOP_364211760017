"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

from labtop import Labtop

# display
def display_labtop():
    if len(my_labtop) == 0:
        print("You had no labtop data")
    else:
        print(f'You had {len(my_labtop)} following: ')
        for x in my_labtop:
            x.display_labtop()
        print("\n")

# option
def display_option_system():
    select = 0
    print("Welcome to Labtop Data Store System (VDSS)")
    print("1.Add Labtop")
    print("2.Display all Labtop")
    print("3.Exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_labtop_data()
    elif select == 2:
        display_labtop()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")

# input data
def input_labtop_data():
    no = int(input("Enter Labtop No: "))
    brand = input("Enter Labtop Brand: ")
    model = input("Enter Labtop Model: ")
    cpu = input("Enter Labtop CPU: ")
    ram = int(input("Enter Labtop RAM(GB): "))
    display = float(input("Enter Labtop Display(inch): "))
    storage = int(input("Enter Labtop Storage(GB): "))
    price = int(input("Enter Labtop Price: "))

    #return no, brand, model, cpu, ram, display, storage, price #return as tuple
    my_labtop.append(Labtop(no, brand, model, cpu, ram, display, storage, price))
    print("\n-------------------------------------")
    print("Already add laptop to store.")
    print("-------------------------------------")

my_labtop = []
s = 0
while s == 0:
    display_option_system()

