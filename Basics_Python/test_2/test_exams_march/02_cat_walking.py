minutes_per_day = int(input())
number_of_walks = int(input())
number_of_calories = int(input())

cat_walk = (minutes_per_day * number_of_walks) * 5
calories = number_of_calories * 0.5

if cat_walk >= calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {cat_walk}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {cat_walk}.")