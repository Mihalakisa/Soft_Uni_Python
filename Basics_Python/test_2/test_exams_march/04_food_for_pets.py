days = int(input())
food = float(input())
dog_food = 0
cat_food = 0
total_food = 0
biscuits = 0

for i in range(1, days + 1):
    eaten_dog_food = int(input())
    eaten_cat_food = int(input())

    if i % 3 == 0:
        biscuits = (eaten_dog_food + eaten_cat_food) * 0.1

    dog_food += eaten_dog_food
    cat_food += eaten_cat_food
    total_food = dog_food + cat_food

percent_food = abs(total_food / food) * 100
percent_dog = abs(dog_food / total_food) * 100
percent_cat = abs(cat_food / total_food) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percent_food:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")