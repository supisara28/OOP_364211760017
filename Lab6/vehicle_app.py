from vehicle import Vehicle

# display
def display_vehicle():
    if len(my_vehicle) == 0:
        print("You had no vehicle data")
    else:
        print(f'You had {len(my_vehicle)} following: ')
        for x in my_vehicle:
            x.vehicle_detail()
        print("\n")

# option
def display_option():
    select = 0
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Display all Vehicle")
    print("3.Exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")



# input data
def input_vehicle_data():
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = int(input("Enter vehicle max speed: "))
    price = float(input("Enter vehicle price: "))

    #return brand, model, color, maxspeed, price #return as tuple
    my_vehicle.append(Vehicle(brand, model, color, maxspeed, price))
    print("\n-------------------------------------")
    print("Already add vehicle to store.")
    print("-------------------------------------")

my_vehicle = []
s = 0
while s == 0:
    display_option()






#vm = input_vehicle_data()
#print(vm)
#print(type(vm))
#create object of Vehicle class
#v1 = Vehicle(vm[0], vm[1], vm[2], vm[3], vm[4])
#display all object attributes
#v1.vehicle_detai()

#vm = input_vehicle_data()
#print(vm)
#print(type(vm))
#create object of Vehicle class
#v2 = Vehicle(vm[0], vm[1], vm[2], vm[3], vm[4])
#display all object attributes
#v2.vehicle_detai()