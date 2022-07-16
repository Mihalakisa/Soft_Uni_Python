import sys

pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health_ship = int(input())
count_repair = 0
percent_health = max_health_ship * (20/100)
pirate_health = 0

while True:
    line = input()
    if line == 'Retire':
        pirate_sum = sum(pirate_ship)
        warship_sum = sum(warship)
        print(f"Pirate ship status: {pirate_sum}")
        print(f"Warship status: {warship_sum}")
        break

    elif line == 'Status':
        for health in range(len(pirate_ship)):
            if pirate_ship[health] < percent_health:
                count_repair += 1
        print(f"{count_repair} sections need repair.")
        continue

    explode = line.split(' ')
    command = explode[0]
    start_index = int(explode[1])
    end_index = int(explode[2])

    if command == 'Fire':
        if 0 <= start_index < (len(warship)):
            warship[start_index] -= end_index
            if warship[start_index] <= 0:
                print("You won! The enemy ship has sunken.")
                sys.exit()

    elif command == 'Defend':
        damage_ws = int(explode[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for health in range(start_index, end_index + 1):
                pirate_ship[health] -= damage_ws
                if pirate_ship[health] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    sys.exit()

    elif command == 'Repair':
        if 0 <= start_index < len(pirate_ship):
            pirate_ship[start_index] += end_index
            if pirate_ship[start_index] > max_health_ship:
                pirate_ship[start_index] = max_health_ship
