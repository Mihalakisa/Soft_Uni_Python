number_km = int(input())
tariff = input()

price = 0
if number_km < 20:
    if tariff == "day":
        price = 0.70 + number_km * 0.79

    else:
        price = 0.70 + number_km * 0.90

elif 20 <= number_km < 100:
    price = 0.09 * number_km

elif 100 <= number_km:
    price = 0.06 * number_km

print(f'{price:.2f}')