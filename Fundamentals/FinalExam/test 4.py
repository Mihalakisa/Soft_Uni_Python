heroes_dict = dict()

while True:
    info = input()
    if info == 'End':
        break

    data = info.split(' ')
    command = data[0]
    hero_name = data[1]

    if command == 'Enroll':
        if hero_name not in heroes_dict:
            heroes_dict[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif command == 'Learn':
        spell_name = data[2]
        if hero_name not in heroes_dict:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name not in heroes_dict[hero_name]:
                heroes_dict[hero_name] += [spell_name]
            else:
                print(f"{hero_name} has already learnt {spell_name}.")

    elif command == 'Unlearn':
        spell_name = data[2]
        if hero_name not in heroes_dict:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes_dict[hero_name]:
                heroes_dict[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
heroes_dict.
print('Heroes:')
for key, value in heroes_dict.items():
    if len(value) == 0:
        print(f"== {key}:")
    else:
        print(f"== {key}:", end=" "),
        for val in value:
            if val == value[len(value) - 1]:
                print(val)
            else:
                print(val, end=", ")
