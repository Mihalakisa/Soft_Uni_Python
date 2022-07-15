# 01 The Hunting Games
days = int(input())
num_players = int(input())
energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

total_water = days * num_players * water_per_day
total_food = days * num_players * food_per_day


for day in range(1, days + 1):
    energy_loss = float(input())

    energy -= energy_loss
    if energy <= 0:
        break

    if day % 2 == 0:
        energy += (energy * (5/100))
        total_water -= (total_water * (30/100))

    if day % 3 == 0:
        energy += (energy * (10 / 100))
        total_food -= total_food / num_players

if energy <= 0:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
