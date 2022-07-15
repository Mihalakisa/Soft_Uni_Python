budget = float(input())
price_1kg_flour = float(input())
bread_count = 0
eggs_count = 0

pack_of_eggs = price_1kg_flour * 0.75
liter_milk = price_1kg_flour + (price_1kg_flour * 0.25)
bread = pack_of_eggs + price_1kg_flour + (liter_milk/4)

while budget > bread:
    budget = budget - bread
    bread_count += 1
    eggs_count += 3

    if bread_count % 3 == 0:
        eggs_count = (eggs_count - (bread_count - 2))

print(f"You made {bread_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget:.2f}BGN left.")