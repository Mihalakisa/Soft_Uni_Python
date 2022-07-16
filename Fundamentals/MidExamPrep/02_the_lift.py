people_waiting = int(input())
lift_space = input().split(' ')
lift_space = list(map(int, lift_space))
max_space_lift = 4
condition = False
free_space_condition = False
people_queue_condition = False

for space in range(len(lift_space)):
    if people_waiting < 4:
        if lift_space[space] == 0:
            lift_space[space] = people_waiting
            people_waiting -= people_waiting
        else:
            max_space_lift -= lift_space[space]
            people_waiting -= max_space_lift
            lift_space[space] += max_space_lift
    else:
        if lift_space[space] == 0:
            people_waiting -= 4
            lift_space[space] = 4
        else:
            max_space_lift -= lift_space[space]
            people_waiting -= max_space_lift
            lift_space[space] += max_space_lift

    max_space_lift = 4

for full in range(len(lift_space)):
    if lift_space[full] == 4 and people_waiting == 0:
        condition = True
    elif lift_space[full] != 4 and people_waiting == 0:
        condition = False
        free_space_condition = True
    elif lift_space[full] == 4 and people_waiting != 0:
        people_queue_condition = True


if free_space_condition:
    print("The lift has empty spots!")
    print(*lift_space, sep=' ')
elif people_queue_condition:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift_space, sep=' ')
elif condition:
    print(*lift_space, sep=' ')
