line = input()
net_price = 0

while line != 'special' and line != 'regular':
    current_price = float(line)

    if current_price > 0:
        net_price += current_price
    else:
        print("Invalid price!")

    line = input()

if net_price <= 0:
    print("Invalid order!")
else:
    taxes = net_price * 0.2
    final_price = net_price + taxes

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")

    if line == 'special':
        final_price = final_price * 0.9

    print(f"Total price: {final_price:.2f}$")
