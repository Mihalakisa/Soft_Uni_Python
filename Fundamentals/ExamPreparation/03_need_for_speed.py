num_cars = int(input())
cars = dict()
diff_fuel = 0

for i in range(num_cars):
    text = input().split('|')
    car = text[0]
    mileage = int(text[1])
    fuel = int(text[2])
    cars[car] = [mileage, fuel]

while True:
    text = input()
    if text == 'Stop':
        break

    data = text.split(' : ')
    command = data[0]
    car = data[1]

    if command == 'Drive':
        distance = int(data[2])
        fuel = int(data[3])
        if cars[car][1] >= fuel:
            cars[car][1] -= fuel
            cars[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

    elif command == 'Refuel':
        fuel = int(data[2])
        cars[car][1] += fuel
        if cars[car][1] > 75:
            diff_fuel = cars[car][1] - 75
            diff_fuel = abs(fuel - diff_fuel)
            cars[car][1] = 75
            print(f"{car} refueled with {diff_fuel} liters")
        else:
            print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        kilometers = int(data[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in cars.keys():
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")