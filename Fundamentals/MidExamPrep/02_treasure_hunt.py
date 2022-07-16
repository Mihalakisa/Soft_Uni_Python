treasure_chest = input().split('|')
loot_count = 0
condition = False
stolen_list = []

while True:
    line = input()

    if line == 'Yohoho!':
        if len(treasure_chest) <= 0:
            print("Failed treasure hunt.")
            break
        else:
            condition = True
            break

    explode = line.split(' ')
    command = explode[0]
    index_number = explode[1]

    if command == 'Loot':
        for index in range(1, len(explode)):
            index = explode[index]
            if index not in treasure_chest:
                treasure_chest.insert(0, index)
        loot_count += 1

    elif command == 'Drop':
        if int(index_number) < len(treasure_chest):
            current_index = treasure_chest[int(index_number)]
            treasure_chest.pop(int(index_number))
            treasure_chest.append(current_index)

    elif command == 'Steal':
        # if loot_count <= int(index_number):
        stolen_list = treasure_chest[-int(index_number):]
        print(', '.join(stolen_list))
        del treasure_chest[-int(index_number):]

if condition:
    sum_items = 0
    for item in range(len(treasure_chest)):
        sum_items += len(treasure_chest[item])

    diff = sum_items / len(treasure_chest)
    print(f"Average treasure gain: {diff:.2f} pirate credits.")
