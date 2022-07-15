from collections import deque

materials = [int(x) for x in input().split(' ')]
magic_levels = deque([int(x) for x in input().split(' ')])

gemstone = 'Gemstone'
porcelain_sculpture = 'Porcelain Sculpture'
gold = 'Gold'
diamond_jewellery = 'Diamond Jewellery'
result = {}
gem_condition = False
sculpture_condition = False
gold_condition = False
diamond_condition = False

while materials and magic_levels:
    material = materials.pop()
    magic_lvl = magic_levels.popleft()

    sum_number = material + magic_lvl

    if sum_number < 100:
        if sum_number % 2 == 0:
            sum_number = (material * 2) + (magic_lvl * 3)
        else:
            sum_number *= 2
    if sum_number > 499:
        sum_number /= 2
    if 100 <= sum_number <= 199:
        if gemstone not in result:
            result[gemstone] = 0
        result[gemstone] += 1
        gem_condition = True
    elif 200 <= sum_number <= 299:
        if porcelain_sculpture not in result:
            result[porcelain_sculpture] = 0
        result[porcelain_sculpture] += 1
        sculpture_condition = True
    elif 300 <= sum_number <= 399:
        if gold not in result:
            result[gold] = 0
        result[gold] += 1
        gold_condition = True
    elif 400 <= sum_number <= 499:
        if diamond_jewellery not in result:
            result[diamond_jewellery] = 0
        result[diamond_jewellery] += 1
        diamond_condition = True

if gem_condition and sculpture_condition or gold_condition and diamond_condition:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
for key, value in sorted(result.items()):
    print(f"{key}: {value}")