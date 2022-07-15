# 02 Space Travel
route = input()
explode = [game.split(' ') for game in route.split('||')]
fuel = int(input())
ammo = int(input())
added_fuel = 0
added_ammo = 0

for game in range(len(explode)):
    command = explode[game][0]

    if command == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break
    number = explode[game][1]

    if command == 'Travel':
        if fuel >= int(number):
            fuel -= int(number)
            print(f"The spaceship travelled {number} light-years.")
        else:
            print("Mission failed.")
            break

    elif command == 'Enemy':
        if ammo >= int(number):
            ammo -= int(number)
            print(f"An enemy with {number} armour is defeated.")
        elif ammo <= 0 or ammo < int(number):
            fuel -= int(number) * 2
            if fuel > 0:
                print(f"An enemy with {number} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif command == 'Repair':
        added_fuel = int(number)
        added_ammo = int(number) * 2
        fuel += added_fuel
        ammo += added_ammo
        print(f"Ammunitions added: {added_ammo}.")
        print(f"Fuel added: {added_fuel}.")
