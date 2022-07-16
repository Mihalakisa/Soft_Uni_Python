food_kg = float(input()) * 1000
hay_kg = float(input()) * 1000
cover_kg = float(input()) * 1000
puppy_weight = float(input()) * 1000
count_day = 0

while True:
    count_day += 1
    food_kg -= 300

    if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
        print("Merry must go to the pet store!")
        break

    if count_day % 2 == 0:
        hay_kg -= food_kg * (5/100)

    if count_day % 3 == 0:
        cover_kg -= puppy_weight * (1/3)

    if count_day == 30:
        print(f"Everything is fine! Puppy is happy! Food: {(food_kg/1000):.2f}, "
              f"Hay: {(hay_kg/1000):.2f}, Cover: {(cover_kg/1000):.2f}.")
        break
