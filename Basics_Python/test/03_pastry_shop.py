cake = input()
ordered_cakes = int(input())
day_of_december = int(input())
price = 0

if day_of_december <= 15:
    if cake == 'Cake':
        price = 24
    elif cake == 'Souffle':
        price = 6.66
    elif cake == 'Baklava':
        price = 12.60
elif 15 < day_of_december:
    if cake == 'Cake':
        price = 28.70
    elif cake == 'Souffle':
        price = 9.80
    elif cake == 'Baklava':
        price = 16.98

total_price = price * ordered_cakes

if day_of_december <= 22:
    if 100 <= total_price <= 200:
        total_price = total_price - (total_price * 0.15)
    elif 200 < total_price:
        total_price = total_price - (total_price * 0.25)

if day_of_december <= 15:
    total_price = total_price - (total_price * 0.1)

print(f"{total_price:.2f}")