type_of_fuel = input()
amount_of_fuel = float(input())
club_card = input()

if type_of_fuel == "Gas":
    if club_card == "Yes":
        price = 0.93 - 0.08
        full_price = price * amount_of_fuel
        if amount_of_fuel < 20:
            print(f'{full_price:.2f} lv.')
        elif 20 <= amount_of_fuel <= 25:
            discount_price = full_price - full_price * 0.08
            print(f'{discount_price:.2f} lv.')
        elif 25 < amount_of_fuel:
            discount_price = full_price - full_price * 0.1
            print(f'{discount_price:.2f} lv.')
    elif club_card == "No":
        full_price = 0.93 * amount_of_fuel
        if amount_of_fuel < 20:
            print(f'{full_price:.2f} lv.')
        elif 20 <= amount_of_fuel <= 25:
            discount_price = full_price - full_price * 0.08
            print(f'{discount_price:.2f} lv.')
        elif 25 < amount_of_fuel:
            discount_price = full_price - full_price * 0.1
            print(f'{discount_price:.2f} lv.')

elif type_of_fuel == "Gasoline":
    if club_card == "Yes":
        price = 2.22 - 0.18
        full_price = price * amount_of_fuel
        if amount_of_fuel < 20:
            print(f'{full_price:.2f} lv.')
        elif 20 <= amount_of_fuel <= 25:
            discount_price = full_price - full_price * 0.08
            print(f'{discount_price:.2f} lv.')
        elif 25 < amount_of_fuel:
            discount_price = full_price - full_price * 0.1
            print(f'{discount_price:.2f} lv.')
    elif club_card == "No":
        full_price = 2.22 * amount_of_fuel
        if amount_of_fuel < 20:
            print(f'{full_price:.2f} lv.')
        elif 20 <= amount_of_fuel <= 25:
            discount_price = full_price - full_price * 0.08
            print(f'{discount_price:.2f} lv.')
        elif 25 < amount_of_fuel:
            discount_price = full_price - full_price * 0.1
            print(f'{discount_price:.2f} lv.')

elif type_of_fuel == "Diesel":
    if club_card == "Yes":
        price = 2.33 - 0.12
        full_price = price * amount_of_fuel
        if amount_of_fuel < 20:
            print(f'{full_price:.2f} lv.')
        elif 20 <= amount_of_fuel <= 25:
            discount_price = full_price - full_price * 0.08
            print(f'{discount_price:.2f} lv.')
        elif 25 < amount_of_fuel:
            discount_price = full_price - full_price * 0.1
            print(f'{discount_price:.2f} lv.')
    elif club_card == "No":
        full_price = 2.33 * amount_of_fuel
        if amount_of_fuel < 20:
            print(f'{full_price:.2f} lv.')
        elif 20 <= amount_of_fuel <= 25:
            discount_price = full_price - full_price * 0.08
            print(f'{discount_price:.2f} lv.')
        elif 25 < amount_of_fuel:
            discount_price = full_price - full_price * 0.1
            print(f'{discount_price:.2f} lv.')