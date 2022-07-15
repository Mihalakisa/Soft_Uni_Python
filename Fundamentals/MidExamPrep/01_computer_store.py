price_no_tax = 0
taxes = 0
total_price = 0

while True:
    command = input()

    if command == 'special':
        if total_price == 0:
            print("Invalid order!")
            break
        diff = total_price - (total_price * 0.1)
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_no_tax:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {diff:.2f}$")
        break
    elif command == 'regular':
        if total_price == 0:
            print("Invalid order!")
            break

        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_no_tax:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")
        break

    part_prices = float(command)

    if part_prices < 0:
        print("Invalid price!")
        continue

    price_no_tax += part_prices
    taxes = price_no_tax * (20/100)
    total_price = taxes + price_no_tax
