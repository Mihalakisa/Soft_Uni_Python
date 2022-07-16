budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_extra_cost = int(input())

if number_of_nights > 7:
    price_per_night = price_per_night - (0.05 * price_per_night)

all_nights_cost = price_per_night * number_of_nights
extra_costs = budget * (percent_extra_cost / 100)
all_sum = all_nights_cost + extra_costs

diff = abs(budget - all_sum)
if budget >= all_sum:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")

else:
    print(f"{diff:.2f} leva needed.")