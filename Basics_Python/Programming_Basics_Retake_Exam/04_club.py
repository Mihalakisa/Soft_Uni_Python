desired_money = float(input())
all_order = 0
diff = 0
order = 0

while True:
    cocktail = input()

    if cocktail == 'Party!':
        if desired_money > all_order:
            diff = desired_money - all_order
            print(f"We need {diff:.2f} leva more.")
            print(f"Club income - {all_order:.2f} leva.")
        else:
            print("Target acquired.")
            print(f"Club income - {all_order:.2f} leva.")
        break

    number_of_cocktails = int(input())

    cocktail_price = len(cocktail)
    order = cocktail_price * number_of_cocktails

    if order % 2 != 0:
        order = order - (order * 0.25)

    all_order += order
    order = 0

    if desired_money <= all_order:
        print("Target acquired.")
        print(f"Club income - {all_order:.2f} leva.")
        break