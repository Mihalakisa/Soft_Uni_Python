type_fuel = input()
liters_fuel = float(input())

if type_fuel == "Diesel":
    if liters_fuel >= 25:
        print("You have enough diesel.")
    else:
        print("Fill your tank with diesel!")

elif type_fuel == "Gasoline":
    if liters_fuel >= 25:
        print("You have enough gasoline.")
    else:
        print("Fill your tank with gasoline!")

elif type_fuel == "Gas":
    if liters_fuel >= 25:
        print("You have enough gas.")
    else:
        print("Fill your tank with gas!")

else:
    print("Invalid fuel!")