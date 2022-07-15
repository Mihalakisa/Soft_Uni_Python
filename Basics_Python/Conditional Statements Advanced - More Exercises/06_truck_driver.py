season = input()
km_per_month = float(input())
salary = 0

if km_per_month <= 5000:
    if season in 'Spring Autumn':
        salary = (km_per_month * 0.75) * 4
        salary = salary - (salary * 0.1)
    elif season == 'Summer':
        salary = (km_per_month * 0.90) * 4
        salary = salary - (salary * 0.1)
    elif season == 'Winter':
        salary = (km_per_month * 1.05) * 4
        salary = salary - (salary * 0.1)

elif 5000 < km_per_month <= 10000:
    if season in 'Spring Autumn':
        salary = (km_per_month * 0.95) * 4
        salary = salary - (salary * 0.1)
    elif season == 'Summer':
        salary = (km_per_month * 1.10) * 4
        salary = salary - (salary * 0.1)
    elif season == 'Winter':
        salary = (km_per_month * 1.25) * 4
        salary = salary - (salary * 0.1)

elif 10000 < km_per_month <= 20000:
    if season in 'Spring Summer Autumn Winter':
        salary = (km_per_month * 1.45) * 4
        salary = salary - (salary * 0.1)

print(f"{salary:.2f}")