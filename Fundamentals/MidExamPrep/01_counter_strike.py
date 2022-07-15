max_energy = int(input())
count_won = 0

while True:
    command = input()
    if command == 'End of battle':
        print(f"Won battles: {count_won}. Energy left: {max_energy}")
        break

    distance = int(command)

    if max_energy - distance >= 0:
        max_energy -= distance
        count_won += 1
        if count_won % 3 == 0:
            max_energy += count_won
    else:
        print(f"Not enough energy! Game ends with {count_won} won battles and {max_energy} energy")
        break
