movie_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

if destination == 'Dubai':
    if season == 'Summer':
        price = 40000
    elif season == 'Winter':
        price = 45000

elif destination == 'Sofia':
    if season == 'Summer':
        price = 12500
    elif season == 'Winter':
        price = 17000

elif destination == 'London':
    if season == 'Summer':
        price = 20250
    elif season == 'Winter':
        price = 24000

costs = price * number_of_days

if destination == 'Sofia':
    costs = costs + (costs * 0.25)
elif destination == 'Dubai':
    costs = costs - (costs * 0.3)

diff = abs(movie_budget - costs)
if movie_budget >= costs:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")