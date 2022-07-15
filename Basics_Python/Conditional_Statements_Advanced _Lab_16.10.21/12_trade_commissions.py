town = input()
sales_volume = float(input())

s = 0
if town == "Sofia":
    if 0 <= sales_volume <= 500:
        s = 5/100
    elif 500 < sales_volume <= 1000:
        s = 7/100
    elif 1000 < sales_volume <= 10000:
        s = 8/100
    elif sales_volume > 10000:
        s = 12/100
elif town == "Varna":
    if 0 <= sales_volume <= 500:
        s = 4.5/100
    elif 500 < sales_volume <= 1000:
        s = 7.5/100
    elif 1000 < sales_volume <= 10000:
        s = 10/100
    elif sales_volume > 10000:
        s = 13/100
elif town == "Plovdiv":
    if 0 <= sales_volume <= 500:
        s = 5.5 / 100
    elif 500 < sales_volume <= 1000:
        s = 8 / 100
    elif 1000 < sales_volume <= 10000:
        s = 12 / 100
    elif sales_volume > 10000:
        s = 14.5 / 100

if s != 0:
    sum = sales_volume * s
    print(f"{sum:.2f}")
else:
    print("error")