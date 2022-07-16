drink = input()
sugar = input()
number_of_drinks = int(input())

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1.00
    elif sugar == 'Extra':
        price = 1.20

elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1.00
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60

elif drink == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

coffee_cost = number_of_drinks * price

if sugar == 'Without':
    coffee_cost = coffee_cost - (coffee_cost * 0.35)

if drink == 'Espresso' and number_of_drinks >= 5:
    coffee_cost = coffee_cost - (coffee_cost * 0.25)

if coffee_cost > 15:
    coffee_cost = coffee_cost - (coffee_cost * 0.2)

print(f"You bought {number_of_drinks} cups of {drink} for {coffee_cost:.2f} lv.")