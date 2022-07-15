counter = int(input())
parking_car_dict = {}

for i in range(counter):
    info = input().split(' ')
    command = info[0]
    name = info[1]

    if command == 'register':
        car_number = info[2]
        if name not in parking_car_dict:
            parking_car_dict[name] = car_number
            print(f"{name} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_number}")

    elif command == 'unregister':
        if name in parking_car_dict:
            parking_car_dict.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for key, value in parking_car_dict.items():
    print(f"{key} => {value}")
