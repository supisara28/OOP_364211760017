"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

from labtop import Labtop

# display
def display_labtop():
    if len(my_labtop) == 0:
        print("\nYou had no labtop data.\n")
    else:
        num = 1
        print(f'You had {len(my_labtop)} following: ')
        for x in my_labtop:
            print(f'{num}. ', end="")
            x.display_labtop()
            num += 1
        print("\n")

# option
def display_option_system():
    select = 0
    print("Welcome to Labtop Data Store System (LDSS)")
    print("1.Add Labtop")
    print("2.Display all Labtop")
    print("3.Delete Labtop")
    print("4.Edit Labtop Price")
    print("5.Exit")
    select = int(input("select(1-5)? : "))
    if select == 1:
        input_labtop_data()
    elif select == 2:
        display_labtop()
    elif select == 3:
        delete_labtop()
    elif select == 4:
        edit_labtop_price()
    elif select == 5:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-5.")

# edit data
def edit_labtop_price():
    print("Which one do you want to edit price?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:? "))
        if s in range(1, n + 1):
            print(f'old price: {my_labtop[s-1].get_price()}')
            newprice = float(input("enter new price: "))
            my_labtop[s-1].set_price(newprice)
            print("\nLaptop price updated.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please, select number 1-{n} ro type 0 to main options.")


# delete data
def delete_labtop():
    print("Which one do you want to remove?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:? "))
        if s in range(1, n+1):
            my_labtop.pop(s-1)
            print("\nAlready delete laptop data.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please, select number 1-{n} ro type 0 to main options.")

# input data
def input_labtop_data():
    brand = input("Enter Labtop Brand: ")
    model = input("Enter Labtop Model: ")
    cpu = input("Enter Labtop CPU: ")
    ram = int(input("Enter Labtop RAM(GB): "))
    display = float(input("Enter Labtop Display(inch): "))
    storage = int(input("Enter Labtop Storage(GB): "))
    price = float(input("Enter Labtop Price: "))

    l = Labtop("", "", "", 0, 0, 0, 0)

    l.set_brand(brand)
    l.set_model(model)
    l.set_cpu(cpu)
    l.set_ram(ram)
    l.set_display(display)
    l.set_storage(storage)
    l.set_price(price)

    # return no, brand, model, cpu, ram, display, storage, price #return as tuple
    # my_labtop.append(Labtop(brand, model, cpu, ram, display, storage, price))
    my_labtop.append(l)
    print("\n-------------------------------------")
    print("Already add laptop to store.")
    print("-------------------------------------")

my_labtop = []
my_labtop.append(Labtop("AUSU","Vivobook 15x","Intel Core i5-12500H",8,15.6,512,27990))
my_labtop.append(Labtop("Lenovo","IdeaPad Gaming3","Intel Core i5-11320H",8,15.6,512,25990))
# my_labtop.append(Labtop("Acer","Swift3","Intel Core i7-1260P","8","14","512","33990"))
s = 0
while s == 0:
    display_option_system()

