budget = float(input())
fuel_needed = float(input())
day_from_week = input()

fuel_plus_guide_price = fuel_needed * 2.10 + 100

if day_from_week == 'Saturday':
    price = fuel_plus_guide_price - (fuel_plus_guide_price * 0.1)

elif day_from_week == 'Sunday':
    price = fuel_plus_guide_price - (fuel_plus_guide_price * 0.2)
else:
    price = fuel_plus_guide_price

diff = abs(budget - price)
if budget >= price:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")