number = int(input())
plant_dict = dict()

for i in range(number):
    text = input().split('<->')
    plant = text[0]
    rarity = int(text[1])
    if plant not in plant_dict:
        plant_dict[plant] = []
        plant_dict[plant].append(rarity)
    else:
        plant_dict[plant][0] = rarity

while True:
    text = input()
    if text == 'Exhibition':
        break

    data = text.split(': ')
    command = data[0]
    other = data[1]

    if command == 'Rate':
        plant, rating = other.split(' - ')
        if plant in plant_dict:
            if len(plant_dict[plant]) < 2:
                plant_dict[plant].append(int(rating))
            else:
                plant_dict[plant][1] += int(rating)
                plant_dict[plant][1] /= 2
        else:
            print('error')

    elif command == 'Update':
        plant, rarity = other.split(' - ')
        if plant in plant_dict:
            plant_dict[plant][0] = int(rarity)
        else:
            print('error')

    elif command == 'Reset':
        if other in plant_dict:
            plant_dict[other][1] = 0
        else:
            print('error')

print("Plants for the exhibition:")
for plant in plant_dict.keys():
    print(f"- {plant}; Rarity: {plant_dict[plant][0]}; Rating: {plant_dict[plant][1]:.2f}")
