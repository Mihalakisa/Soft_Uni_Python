budget = float(input())
season = input()
price = 0

if budget <= 1000:
    if season == 'Summer':
        price = budget * 0.65
        print(f"Alaska - Camp - {price:.2f}")
    elif season == 'Winter':
        price = budget * 0.45
        print(f"Morocco - Camp - {price:.2f}")

elif 1000 < budget <= 3000:
    if season == 'Summer':
        price = budget * 0.80
        print(f"Alaska - Hut - {price:.2f}")
    elif season == 'Winter':
        price = budget * 0.60
        print(f"Morocco - Hut - {price:.2f}")

elif budget > 3000:
    if season == 'Summer':
        price = budget * 0.90
        print(f"Alaska - Hotel - {price:.2f}")
    elif season == 'Winter':
        price = budget * 0.90
        print(f"Morocco - Hotel - {price:.2f}")