package_kg = float(input())
type_service = input()
distance_km = int(input())
price = 0
markup_price = 0

if type_service == 'standard':
    if package_kg < 1:
        price = 0.03
    elif 1 <= package_kg < 10:
        price = 0.05
    elif 10 <= package_kg < 40:
        price = 0.10
    elif 40 <= package_kg < 90:
        price = 0.15
    elif 90 <= package_kg < 150:
        price = 0.20

elif type_service == 'express':
    if package_kg < 1:
        price = 0.03
        markup_price = 0.03 * 0.8
    elif 1 <= package_kg < 10:
        price = 0.05
        markup_price = 0.05 * 0.4
    elif 10 <= package_kg < 40:
        price = 0.10
        markup_price = 0.10 * 0.05
    elif 40 <= package_kg < 90:
        price = 0.15
        markup_price = 0.15 * 0.02
    elif 90 <= package_kg < 150:
        price = 0.20
        markup_price = 0.20 * 0.01

distance_price = distance_km * price

if type_service == 'standard':
    print(f"The delivery of your shipment with weight of {package_kg:.3f} kg. would cost {distance_price:.2f} lv.")
else:
    markup_km = package_kg * markup_price
    total_markup = distance_km * markup_km
    total_sum = distance_price + total_markup
    print(f"The delivery of your shipment with weight of {package_kg:.3f} kg. would cost {total_sum:.2f} lv.")