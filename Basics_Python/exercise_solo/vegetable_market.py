vegetables_kg = float(input())
fruits_kg = float(input())
total_kg_veg = int(input())
total_kg_fruits = int(input())

vegetables_price = vegetables_kg * total_kg_veg
fruits_price = fruits_kg * total_kg_fruits
total_price = (vegetables_price + fruits_price) / 1.94

print(f"{total_price:.2f}")