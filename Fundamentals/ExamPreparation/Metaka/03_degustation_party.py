command = input()
dictonary = {}
unliked_meals = 0
while command != 'Stop':
    result = command.split('-')
    type = result[0]
    guest = result[1]
    meal = result[2]
    if type == 'Like':
        if guest not in dictonary:
            dictonary[guest] = []

        if meal in dictonary[guest]:
            continue
        dictonary[guest].append(meal)


    elif type == 'Dislike':
        if guest not in dictonary:
            print(f'{guest} is not at the party.')
        elif meal not in dictonary[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            dictonary[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            unliked_meals += 1

    command = input()

dictonary = dict(sorted(dictonary.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in dictonary.items():
    print(f'{key}: {", ".join(x for x in value)}')

print(f'Unliked meals {unliked_meals}')