number_chrysanthemums = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holiday = input()
price = 0

if season == 'Spring':
    price = number_chrysanthemums * 2.00 + number_roses * 4.10 + number_tulips * 2.50
    if holiday == 'Y':
        price = price + (price * 0.15)
        if number_tulips > 7:
            price = price - (price * 0.05)
    elif holiday == 'N':
        if number_tulips > 7:
            price = price - (price * 0.05)

elif season == 'Summer':
    price = number_chrysanthemums * 2.00 + number_roses * 4.10 + number_tulips * 2.50
    if holiday == 'Y':
        price = price + (price * 0.15)
    elif holiday == 'N':
        pass
elif season == 'Autumn':
    price = number_chrysanthemums * 3.75 + number_roses * 4.50 + number_tulips * 4.15
    if holiday == 'Y':
        price = price + (price * 0.15)
    elif holiday == 'N':
        pass
elif season == 'Winter':
    price = number_chrysanthemums * 3.75 + number_roses * 4.50 + number_tulips * 4.15
    if holiday == 'Y':
        price = price + (price * 0.15)
        if number_roses >= 10:
            price = price - (price * 0.1)
    elif holiday == 'N':
        if number_roses >= 10:
            price = price - (price * 0.1)

all_flowers = number_chrysanthemums + number_roses + number_tulips
if all_flowers > 20:
    price = (price - (price * 0.2)) + 2
    print(f"{price:.2f}")
else:
    price = price + 2
    print(f"{price:.2f}")