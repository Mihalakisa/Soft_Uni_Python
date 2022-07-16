age = int(input())
laundry = float(input())
toy_price = int(input())
saved_money = 0
number_of_toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += ((i / 2) * 10) - 1
    else:
        number_of_toys += 1

toys = number_of_toys * toy_price
saved_money = saved_money + toys
diff = abs(saved_money - laundry)

if saved_money >= laundry:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")