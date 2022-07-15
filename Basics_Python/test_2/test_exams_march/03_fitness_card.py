owned_money = float(input())
sex = input()
age = int(input())
sport = input()
sport_cost = 0

if sport == 'Gym':
    if sex == 'm':
        sport_cost = 42
    elif sex == 'f':
        sport_cost = 35

elif sport == 'Boxing':
    if sex == 'm':
        sport_cost = 41
    elif sex == 'f':
        sport_cost = 37

elif sport == 'Yoga':
    if sex == 'm':
        sport_cost = 45
    elif sex == 'f':
        sport_cost = 42

elif sport == 'Zumba':
    if sex == 'm':
        sport_cost = 34
    elif sex == 'f':
        sport_cost = 31

elif sport == 'Dances':
    if sex == 'm':
        sport_cost = 51
    elif sex == 'f':
        sport_cost = 53

elif sport == 'Pilates':
    if sex == 'm':
        sport_cost = 39
    elif sex == 'f':
        sport_cost = 37

if age <= 19:
    sport_cost = sport_cost - (sport_cost * 0.2)

if owned_money >= sport_cost:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(owned_money - sport_cost)
    print(f"You don't have enough money! You need ${diff:.2f} more.")