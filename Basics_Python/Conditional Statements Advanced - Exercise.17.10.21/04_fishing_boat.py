budget = int(input())
season = input()
number_of_fisherman = int(input())
costs = 0

if season == "Spring":
    costs = 3000
    if number_of_fisherman <= 6:
        costs -= costs * 0.10
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05
    elif 7 <= number_of_fisherman <= 11:
        costs -= costs * 0.15
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05
    elif 12 <= number_of_fisherman:
        costs -= costs * 0.25
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05

elif season == "Summer":
    costs = 4200
    if number_of_fisherman <= 6:
        costs -= costs * 0.10
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05
    elif 7 <= number_of_fisherman <= 11:
        costs -= costs * 0.15
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05
    elif 12 <= number_of_fisherman:
        costs -= costs * 0.25
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05

elif season == "Autumn":
    costs = 4200
    if number_of_fisherman <= 6:
        costs -= costs * 0.10
    elif 7 <= number_of_fisherman <= 11:
        costs -= costs * 0.15
    elif 12 <= number_of_fisherman:
        costs -= costs * 0.25

elif season == "Winter":
    costs = 2600
    if number_of_fisherman <= 6:
        costs -= costs * 0.10
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05
    elif 7 <= number_of_fisherman <= 11:
        costs -= costs * 0.15
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05
    elif 12 <= number_of_fisherman:
        costs -= costs * 0.25
        if number_of_fisherman % 2 == 0:
            costs -= costs * 0.05

diff = abs(budget - costs)
if budget >= costs:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")