number = int(input())
plant_dict = dict()

for i in range(number):
    text = input().split('<->')
    plant = text[0]
    rarity = int(text[1])
    plant_dict[plant] = [rarity, 0, 0]

while True:
    text = input()
    if text == 'Exhibition':
        break

    data = text.split(' ')
    command = data[0]
    plant_name = data[1]
    if plant_name not in plant_dict.keys():
        print('error')
        continue

    if command == 'Rate:':
        rating = float(data[3])
        plant_dict[plant_name][1] += rating
        plant_dict[plant_name][2] += 1

    elif command == 'Update:':
        new_rarity = int(data[3])
        plant_dict[plant_name][0] = new_rarity

    elif command == 'Reset:':
        plant_dict[plant_name][1] = 0
        plant_dict[plant_name][2] = 0

print("Plants for the exhibition:")
for plant in plant_dict.keys():
    if plant_dict[plant][2] > 0:
        diff = float((plant_dict[plant][1] / plant_dict[plant][2]))
    else:
        diff = plant_dict[plant][1]
    print(f"- {plant}; Rarity: {plant_dict[plant][0]}; Rating: {diff:.2f}")
