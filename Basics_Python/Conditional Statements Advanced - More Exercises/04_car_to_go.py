budget = float(input())
season = input()
price = 0

if budget <= 100:
    print("Economy class")
    if season == 'Summer':
        price = budget * 0.35
        print(f"Cabrio - {price:.2f}")
    elif season == 'Winter':
        price = budget * 0.65
        print(f"Jeep - {price:.2f}")
elif 100 < budget <= 500:
    print("Compact class")
    if season == 'Summer':
        price = budget * 0.45
        print(f"Cabrio - {price:.2f}")
    elif season == 'Winter':
        price = budget * 0.80
        print(f"Jeep - {price:.2f}")
elif budget > 500:
    print("Luxury class")
    if season in 'Summer Winter':
        price = budget * 0.90
        print(f"Jeep - {price:.2f}")