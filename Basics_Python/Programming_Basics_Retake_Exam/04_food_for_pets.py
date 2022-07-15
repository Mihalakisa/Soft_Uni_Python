number_of_days = int(input())
total_amount_of_food = float(input())
dog_eaten_food = 0
cat_eaten_food = 0
total_eaten_food = 0
biscuits = 0

for i in range(1, number_of_days + 1):
    amount_eaten_dog_food = int(input())
    amount_eaten_cat_food = int(input())

    if i % 3 == 0:
        biscuits += (amount_eaten_dog_food + amount_eaten_cat_food) * 0.1

    dog_eaten_food += amount_eaten_dog_food
    cat_eaten_food += amount_eaten_cat_food

total_eaten_food = dog_eaten_food + cat_eaten_food
percent_eaten_food = (total_eaten_food / total_amount_of_food) * 100
percent_dog_food = (dog_eaten_food / total_eaten_food) * 100
percent_cat_food = (cat_eaten_food / total_eaten_food) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")