years = int(input())
washing_machine = float(input())
toy_price = int(input())
saved_money = 0
number_of_toys = 0

for i in range(1,years + 1):
    if i % 2 == 0:
        saved_money += ((i / 2) * 10) - 1
    else:
        number_of_toys += 1

sold_toys = number_of_toys * toy_price
total_saved_money = saved_money + sold_toys

diff = abs(total_saved_money - washing_machine)
if total_saved_money >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")