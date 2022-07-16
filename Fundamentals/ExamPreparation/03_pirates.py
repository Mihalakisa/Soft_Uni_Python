town_dict = dict()

while True:
    text = input()
    if text == 'Sail':
        break

    data = text.split('||')
    city = data[0]
    people = int(data[1])
    gold = int(data[2])
    if city not in town_dict:
        town_dict[city] = [people, gold]
    else:
        town_dict[city][0] += people
        town_dict[city][1] += gold

while True:
    text = input()
    if text == 'End':
        break

    data = text.split('=>')
    command = data[0]
    city = data[1]
    number_value = int(data[2])

    if command == 'Plunder':
        gold = int(data[3])
        if city in town_dict:
            print(f"{city} plundered! {gold} gold stolen, {number_value} citizens killed.")
            town_dict[city][0] -= number_value
            town_dict[city][1] -= gold
            if town_dict[city][0] <= 0 or town_dict[city][1] <= 0:
                print(f"{city} has been wiped off the map!")
                del town_dict[city]

    elif command == 'Prosper':
        if number_value < 0:
            print("Gold added cannot be a negative number!")
        else:
            if city in town_dict:
                town_dict[city][1] += number_value
                print(f"{number_value} gold added to the city treasury. {city} now has {town_dict[city][1]} gold.")

town_count = int(len(town_dict.keys()))

if not town_dict:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {town_count} wealthy settlements to go to:")
    for town in town_dict:
        print(f"{town} -> Population: {town_dict[town][0]} citizens, Gold: {town_dict[town][1]} kg")