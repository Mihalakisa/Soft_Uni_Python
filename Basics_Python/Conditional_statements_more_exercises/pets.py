import math

days = int(input())
left_food = int(input())
food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input())

needed_food_for_dog = days * food_per_day_dog
needed_food_for_cat = days * food_per_day_cat
needed_food_for_turtle = (days * food_per_day_turtle) / 1000
total_food = needed_food_for_dog + needed_food_for_cat + needed_food_for_turtle

if total_food <= left_food:
    remaining_food = math.floor(left_food - total_food)
    print(f'{remaining_food} kilos of food left.')
else:
    food_needed = math.ceil(total_food - left_food)
    print(f'{food_needed} more kilos of food are needed.')